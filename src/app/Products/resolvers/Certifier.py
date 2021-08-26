from . import query, certifier, mutation
from app.Products.schema.Certifier import CertifierDAO
from app.midleware import check_token

certifier.set_alias('id', '_id')


@query.field('certifiers')
def resolve_certifiers(obj, info):
  # manage the filters here
  certifiers = CertifierDAO().list()
  return certifiers


@mutation.field('createCertifier')
@check_token(check_admin=True)
def resolve_create(obj, info, values):
  certifier = CertifierDAO().create(values)
  return certifier
