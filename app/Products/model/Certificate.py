from flask_restx import fields

from app.api import api

CertificateModel = api.model('Certificate', {
    '_id': fields.String(readonly=True, description='The unique certificate registration identifier'),
    'name': fields.String(readonly=True, description='The name of the file'),
    'file': fields.String(required=True, description='The file of the certificate in base64'),
    'companyType': fields.String(description='The type of company that update this file'),
    'companyId': fields.String(description='The id of the company/certifier that create this report'),
})
