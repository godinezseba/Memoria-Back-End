from flask import request

from io import BytesIO
from base64 import b64decode
from pandas import read_csv

from . import query, product, mutation

from app.Products.schema.Product import ProductDAO
from app.Users.midleware import check_token

product.set_alias('id', '_id')


@query.field('products')
def resolve_products(obj, info):
  # manage the filters here
  products = ProductDAO().list()
  return products


@query.field('product')
def resolve_product(obj, info, id):
  product = ProductDAO().get(id)
  return product


@mutation.field('createProductsByFile')
@check_token(check_admin=True)
def resolve_create(obj, info, values):
  file = values.get('file')
  companyId = values.get('companyId')
  columns = values.get('columns')
  separator = values.get('separator', ',')
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
                            index_col=0,
                            sep=separator)
  except Exception as e:
    print(str(e), flush=True)
    raise Exception('Error en la lectura del archivo')

  # check columns in file are the same that the named in the form
  data_columns = list(columns.values())
  file_columns = list(file_decoded.columns)
  if not all(item in data_columns for item in file_columns):
    raise Exception('Faltan columnas en el archivo')

  # change columns names
  try:
    new_values = {
        columns.get('name'): 'name',
        columns.get('barCode'): 'barCode',
        columns.get('externalId'): 'externalId',
        columns.get('CO2'): 'CO2',
        columns.get('water'): 'water',
    }
    file_decoded.rename(columns=new_values, inplace=True)
  except Exception as e:
    print(str(e), flush=True)
    raise Exception('Faltan columnas en el formulario')

  # extract the id of the company to be place in the products data
  new_values_created = []
  for _, row in file_decoded.iterrows():
    new_product = row.to_dict()
    new_product['companyId'] = companyId
    new_product['ratingData'] = {
        'CO2': new_product.pop('CO2'),
        'water': new_product.pop('water'),
    }
    new_values_created.append(ProductDAO().create(new_product))

  return True
