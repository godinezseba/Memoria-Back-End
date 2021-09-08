from . import query, file
from app.Products.schema.File import FileDAO

file.set_alias('id', '_id')

fileDAO = FileDAO()


@query.field('file')
def resolve_file(obj, info, id):
  print("entre", flush=True)
  file = fileDAO.get_one(id)
  return file
