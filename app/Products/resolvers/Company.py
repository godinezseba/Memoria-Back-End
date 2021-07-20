from flask import request

from . import query, company, mutation
from app.Products.schema.Company import CompanyDAO
from app.Users.midleware import check_token

company.set_alias('id', '_id')


def add_company_info(data, user):
  """
  Helper function to add extra information in the certificates
  """
  data['companyType'] = user['companyType']
  data['companyId'] = user['companyId']
  return data


@query.field('companies')
def resolve_companies(obj, info):
  # manage the filters here
  products = CompanyDAO().list()
  return products


@query.field('company')
def resolve_company(obj, info, id):
  product = CompanyDAO().get(id)
  return product


@mutation.field('createCompany')
@check_token(check_admin=True)
def resolve_create(obj, info, values):
  user = request.user_data
  # add origin info
  values['actions'] = [add_company_info(
      action, user) for action in values.get('actions', [])]
  values['certificates'] = [add_company_info(
      action, user) for action in values.get('certificates', [])]
  return CompanyDAO().create(values)
