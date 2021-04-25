from flask_restx import fields

from . import api

CertifierModel = api.model('Certifier', {
    'name': fields.String(required=True, description='The barcode for this product id, in EAN-13 format'),
    'country': fields.String(required=True, description='The main country of the certifier'),
    'description': fields.String(required=True, description='A short description of the company/foundation'),
    'picture': fields.String(description='The logo of the certifier')
})
