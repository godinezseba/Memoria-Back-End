from flask_restx import fields

from app.api import api
from .Certificate import CertificateModel

CompanyModel = api.model('Company', {
    '_id': fields.String(readonly=True, description='The unique company registration identifier'),
    'name': fields.String(required=True, description='The name of the company'),
    'country': fields.String(description='The main country of the company'),
    'carbonFootPrint': fields.Float(description='The CO2 produced by this company'),
    'description': fields.String(description='A short description of the company'),
    'picture': fields.String(description='The logo of the company'),
    'certificates': fields.List(fields.Nested(CertificateModel))
})
