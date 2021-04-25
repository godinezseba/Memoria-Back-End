from flask_restx import fields

from . import api

CertificateModel = api.model('Certificate', {
  'file': fields.String(required=True, description='The file of the certificate in base64'),
  'certifier': fields.Integer(required=True, description='The certifier that create this report'),
})
