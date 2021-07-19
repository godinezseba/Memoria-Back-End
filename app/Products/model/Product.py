from flask_restx import fields

from app.api import api
from .Rating import RatingModel

ProductModel = api.model('Product', {
    'id': fields.String(description='The unique product registration identifier', attribute='_id'),
    'barCode': fields.String(required=True, description='The barcode for this product id, in EAN-13 format'),
    'name': fields.String(required=True, description='The name of the product'),
    'companyId': fields.String(required=True, description='An external id provided to this product'),
    'externalId': fields.String(description='The id of the company of this product'),
    'ratingData': fields.Nested(RatingModel)
})

# GraphQL schema
ProductSchema = """
  type Product {
    id: Int!
    barCode: Int!
    name: String!
    companyId: String!
    externalId: String
    rating: Rating
  } 
"""
