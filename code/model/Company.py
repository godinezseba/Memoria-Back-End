from flask_restx import fields

from . import api
from .Certificate import CertificateModel

CompanyModel = api.model('Company', {
    'name': fields.String(required=True, description='The name of the company'),
    'country': fields.String(required=True, description='The main country of the company'),
    'description': fields.String(required=True, description='A short description of the company/foundation'),
    'picture': fields.String(description='The logo of the company'),
    'certificates': fields.List(fields.Nested(CertificateModel))
})
