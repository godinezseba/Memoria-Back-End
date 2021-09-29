from flask import request

from . import query, company, mutation, action, certificate
from app.Products.schema.Company import CompanyDAO
from app.Products.schema.File import FileDAO
from app.midleware import check_token

from app.redisClient import queue
from app.Products.workers.Company.label import create_label

company.set_alias('id', '_id')

companyDAO = CompanyDAO()
fileDAO = FileDAO()


def add_company_info(data, user):
  """
  Helper function to add extra information in the certificates
  """
  if not (data.get('companyType') or data.get('companyId')):
    data['companyType'] = user['companyType']
    data['companyId'] = user['companyId']
  if data.get('file'):
    del data['file']
  return data


@query.field('companies')
@check_token(raise_on_null=False)
def resolve_companies(obj, info, onlyEditable=False):
  if onlyEditable:
    try:
      user = request.user_data
      if user.get('isAdmin'):
        companies = companyDAO.list()
        return companies
      companies = companyDAO.list(
          filters={'ids': user.get('editableCompanies', [])})
      return companies
    except:
      raise Exception('Necesita permisos')
  companies = companyDAO.list()
  return companies


@query.field('company')
def resolve_company(obj, info, id):
  company = companyDAO.get_one(id)
  return company


@mutation.field('createCompany')
@check_token(check_admin=True)
def resolve_create(obj, info, values):
  user = request.user_data
  for key in ['actions', 'certificates']:
    new_files = values.get(key, [])
    if len(new_files):
      # create file
      new_ids = fileDAO.create_many(
          [{'file': file['file']} for file in new_files])
      # add file id
      [file.update({'fileId': id}) for id, file in zip(new_ids, new_files)]
      # add origin info and remove file
      values[key] = [add_company_info(action, user) for action in new_files]

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
  for key in ['actions', 'certificates']:
    files = values.get(key, [])
    new_files = [file for file in files if not file.get('fileId')]
    if len(new_files):
      # create files
      new_ids = fileDAO.create_many(
          [{'file': file['file']} for file in new_files])
      # update keys in values[key]
      [file.update({'fileId': id}) for id, file in zip(new_ids, new_files)]
      # add origin info and remove file in case
      values[key] = [add_company_info(
          action, user) for action in files]

  company = companyDAO.update(id, values)
  # add to the queue the labels creation
  queue.enqueue(create_label)
  return company


@action.field('file')
@certificate.field('file')
def resolve_file(obj, info):
  if obj['fileId']:
    file = fileDAO.load(obj['fileId']).get()
    return file['file']
