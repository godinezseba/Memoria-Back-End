from flask_restx import fields

from code.api import api

CertificateModel = api.model('Certificate', {
    'id': fields.String(readonly=True, description='The unique certificate registration identifier'),
    'file': fields.String(required=True, description='The file of the certificate in base64'),
    'certifier': fields.Integer(required=True, description='The certifier that create this report'),
})
