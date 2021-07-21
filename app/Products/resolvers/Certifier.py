from flask import request

from . import query, certifier
from app.Products.schema.Certifier import CertifierDAO

certifier.set_alias('id', '_id')


@query.field('certifiers')
def resolve_certifiers(obj, info):
  # manage the filters here
  certifiers = CertifierDAO().list()
  return certifiers
