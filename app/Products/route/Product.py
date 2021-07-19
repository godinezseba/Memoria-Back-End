from flask import request
from flask_restx import Resource, reqparse

from io import BytesIO
from base64 import b64decode
from pandas import read_csv

from app.api import api
from app.Products.model.Product import ProductModel
from app.Products.schema.Product import ProductDAO
from app.Users.midleware import check_token

product_ns = api.namespace(
    'product', description='User CIR Product Operations')


@product_ns.route('')
class Product(Resource):
  @api.marshal_with(ProductModel)
  @api.doc('List products')
  @api.doc(params={'barcode_id': 'The barcode ID of this product (optional)'})
  def get(self):
    # Currently we support either a full list, or query by barcode_id.
    parser = reqparse.RequestParser()
    parser.add_argument('barcode_id', required=False, location='args')
    args = parser.parse_args()
    if args['barcode_id']:
      return [ProductDAO().get_by_barcode(args['barcode_id'])]
    else:
      return ProductDAO().list()

  @api.marshal_with(ProductModel, code=201)
  @api.doc(body=ProductModel)
  @check_token()
  def post(self):
    actual_user = request.user_data
    new_data = api.payload

    # avoid anyone can add new data
    if (not actual_user.get('isAdmin', False)
            and not new_data.get('company', '') in actual_user.get('editableCompanies', [])):
      api.abort(403)

    # read the file
    try:
      # read only the content
      file_b64 = new_data.get('file', '').split(',')
      if len(file_b64) == 1:
        file_b64 = file_b64[0]
      else:
        file_b64 = file_b64[1]
      # decode and convert to dataframe
      file_decoded = read_csv(BytesIO(b64decode(file_b64)),
                              index_col=0,
                              sep=new_data.get('separator'))
    except Exception as e:
      print(str(e), flush=True)
      api.abort(400, 'Error en la lectura del archivo')

    # check columns in file are the same that the named in the form
    columns = new_data.get('columns')
    if not columns:
      api.abort(400, 'Falta la declaración de columnas en el formulario')
    data_columns = list(columns.values())
    file_columns = list(file_decoded.columns)
    if not all(item in data_columns for item in file_columns):
      api.abort(400, 'Faltan columnas en el archivo')

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
      api.abort(400, 'Faltan columnas en el formulario')

    # extract the id of the company to be place in the products data
    companyId = new_data.get('companyId', '')
    if not companyId:
      api.abort(400, 'Falta el identificador de la empresa (companyId)')

    new_values_created = []
    for _, row in file_decoded.iterrows():
      new_product = row.to_dict()
      new_product['companyId'] = companyId
      new_product['ratingData'] = {
          'CO2': new_product.pop('CO2'),
          'water': new_product.pop('water'),
      }
      new_values_created.append(ProductDAO().create(new_product))

    return new_values_created, 201


@product_ns.route('/<string:id>')
class ProductWithID(Resource):
  @api.marshal_with(ProductModel)
  @api.doc(params={'id': 'The unique ID of this product'})
  def get(self, id):
    print(id, flush=True)
    return ProductDAO().get("123456789")

  @api.marshal_with(ProductModel)
  @api.doc(params={'id': 'The unique ID of this product'})
  @check_token(check_admin=True)
  def delete(self, id):
    return ProductDAO().delete(id)
