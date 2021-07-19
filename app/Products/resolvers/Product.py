from . import query, product
from app.Products.schema.Product import ProductDAO
from app.Users.midleware import check_token

product.set_alias('id', '_id')


@query.field("products")
def resolve_products(obj, info):
  # manage the filters here
  products = ProductDAO().list()
  return products


@query.field("product")
def resolve_product(obj, info, id):
  product = ProductDAO().get(id)
  return product
