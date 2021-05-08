from flask_restx import fields

from app.api import api
from .Certificate import CertificateModel

CompanyModel = api.model('Company', {
    'id': fields.String(readonly=True, description='The unique company registration identifier'),
    'name': fields.String(required=True, description='The name of the company'),
    'country': fields.String(description='The main country of the company'),
    'description': fields.String(description='A short description of the company/foundation'),
    'picture': fields.String(description='The logo of the company'),
    'certificates': fields.List(fields.Nested(CertificateModel))
})
