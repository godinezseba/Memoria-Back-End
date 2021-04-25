from flask_restx import fields

from . import api

CertifierModel = api.model('Certifier', {
    'name': fields.String(required=True, description='The name of the certifier'),
    'country': fields.String(required=True, description='The main country of the certifier'),
    'description': fields.String(required=True, description='A short description of the company/foundation'),
    'picture': fields.String(description='The logo of the certifier')
})
