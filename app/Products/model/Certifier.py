from flask_restx import fields

from app.api import api

CertifierModel = api.model('Certifier', {
    '_id': fields.String(readonly=True, description='The unique company registration identifier'),
    'name': fields.String(required=True, description='The name of the certifier'),
    'country': fields.String(required=True, description='The main country of the certifier'),
    'description': fields.String(description='A short description of the company/foundation'),
    'picture': fields.String(description='The logo of the certifier')
})
