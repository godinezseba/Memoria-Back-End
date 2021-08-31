from flask import request

from . import query, company, mutation
from app.Products.schema.Company import CompanyDAO
from app.midleware import check_token

from app.redisClient import queue
from app.Products.workers.Company.label import create_label

company.set_alias('id', '_id')

companyDAO = CompanyDAO()


def add_company_info(data, user):
  """
  Helper function to add extra information in the certificates
  """
  if not (data.get('companyType') or data.get('companyId')):
    data['companyType'] = user['companyType']
    data['companyId'] = user['companyId']
  return data


@query.field('companies')
def resolve_companies(obj, info):
  # manage the filters here
  products = companyDAO.list()
  return products


@query.field('company')
def resolve_company(obj, info, id):
  product = companyDAO.load(id).get()
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

  company = companyDAO.create(values)
  # add to the queue the labels creation
  queue.enqueue(create_label)
  return company


@mutation.field('updateCompany')
@check_token(check_admin=True)
def resolve_create(obj, info, id, values):
  user = request.user_data
  # avoid that anyone can add new data
  if (not user.get('isAdmin', False)
          and not id in user.get('editableCompanies', [])):
    raise Exception('No tienes permiso para agregar datos a esta empresa')

  # add origin info
  values['actions'] = [add_company_info(
      action, user) for action in values.get('actions', [])]
  values['certificates'] = [add_company_info(
      action, user) for action in values.get('certificates', [])]

  company = companyDAO.update(id, values)
  # add to the queue the labels creation
  queue.enqueue(create_label)
  return company
