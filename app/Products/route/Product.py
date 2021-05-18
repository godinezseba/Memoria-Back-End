from flask_restx import Resource, reqparse

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
  def post(self):
    return ProductDAO().create(api.payload), 201


@product_ns.route('/<string:id>')
class ProductWithID(Resource):
  @api.marshal_with(ProductModel)
  @api.doc(params={'id': 'The unique ID of this product'})
  def get(self, id):
    return ProductDAO().get(id)

  @api.marshal_with(ProductModel)
  @api.doc(params={'id': 'The unique ID of this product'})
  @check_token(check_admin=True)
  def delete(self, id):
    return ProductDAO().delete(id)
