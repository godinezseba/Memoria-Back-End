from . import query, company
from app.Products.schema.Company import CompanyDAO

company.set_alias('id', '_id')


@query.field("companies")
def resolve_companies(obj, info):
  # manage the filters here
  products = CompanyDAO().list()
  return products


@query.field("company")
def resolve_company(obj, info, id):
  product = CompanyDAO().get(id)
  return product
