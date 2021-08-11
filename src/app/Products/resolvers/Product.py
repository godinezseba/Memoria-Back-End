from flask import request

from io import BytesIO
from base64 import b64decode
from pandas import read_csv

from . import query, product, mutation

from app.Products.schema.Product import ProductDAO
from app.Users.midleware import check_token

from app.redisClient import queue
from app.Products.workers.labelCategory import create_label_category
from app.Products.workers.labelGlobal import create_label_global

product.set_alias('id', '_id')


@query.field('products')
def resolve_products(obj, info, filters={}):
  products = ProductDAO().list(filters)
  return products


@query.field('product')
def resolve_product(obj, info, id):
  product = ProductDAO().get(id)
  return product


@mutation.field('updateProduct')
def resolve_update(obj, info, id, data):
  product = ProductDAO().update(id, data)
  return product


@mutation.field('createProductsByFile')
@check_token(check_admin=True)
def resolve_create(obj, info, values):
  file = values.get('file')
  companyId = values.get('companyId')
  columns = values.get('columns')
  separator = values.get('separator', ',')
  otherColumns = values.get('otherColumns', [])

  # check some variables before used them
  if not companyId:
    raise Exception('Falta el identificador de la empresa')

  actual_user = request.user_data

  # avoid that anyone can add new data
  if (not actual_user.get('isAdmin', False)
          and not companyId in actual_user.get('editableCompanies', [])):
    raise Exception('No tienes permiso para agregar datos a esta empresa')

  # read the file
  try:
    # read only the content
    file_b64 = file.split(',')
    if len(file_b64) == 1:
      file_b64 = file_b64[0]
    else:
      file_b64 = file_b64[1]
    # decode and convert to dataframe
    file_decoded = read_csv(BytesIO(b64decode(file_b64)),
                            sep=separator)
  except Exception as e:
    print(str(e), flush=True)
    raise Exception('Error en la lectura del archivo')

  # check columns in file are the same that the named in the form
  data_columns = list(columns.values())
  file_columns = list(file_decoded.columns)
  if not all(item in file_columns for item in data_columns + otherColumns):
    raise Exception('Faltan columnas en el archivo')

  # change columns names
  try:
    new_values = {
        columns['name']: 'name',
        columns['category']: 'category',
        columns['barCode']: 'barCode',
        columns['CO2']: 'CO2',
        columns['water']: 'water',
        columns['forest']: 'deforestation',
    }
    if columns.get('barCodeType'):
      new_values[columns['barCodeType']] = 'barCodeType'
    file_decoded.rename(columns=new_values, inplace=True)
    # only keep columns named
    file_decoded = file_decoded[list(new_values.values()) + otherColumns]
  except Exception as e:
    print(str(e), flush=True)
    raise Exception('Faltan columnas desde el formulario')

  # create a set with all categories added
  categories = set()

  # extract the id of the company to be place in the products data
  def map_products(row):
    new_product = row.to_dict()
    new_product['companyId'] = companyId
    new_product['ratingData'] = {
        'CO2': new_product.pop('CO2'),
        'water': new_product.pop('water'),
        'deforestation': new_product.pop('deforestation'),
    }
    # add other data to the rating
    if len(otherColumns):
      new_product['ratingData']['otherData'] = dict()
    for column in otherColumns:
      new_product['ratingData']['otherData'][column] = new_product.pop(column)
    # add bar code type if not present
    if not columns.get('barCodeType'):
      new_product['barCodeType'] = 'ean13'
    categories.add(new_product['category'])

  ProductDAO().create_many([map_products(row)
                            for _, row in file_decoded.iterrows()])

  jobs = list()
  for category in categories:
    jobs.append(
        queue.enqueue(create_label_category, args=[category], depends_on=jobs))
  queue.enqueue(create_label_global, depends_on=jobs)
  return True
