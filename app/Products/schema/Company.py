from app.api import api
from . import client, DB_COMPANY

# A Data Access Object to handle the reading and writing of Company records to the Cloudant DB


class CompanyDAO(object):
  def __init__(self):
    self.cir_db = client[DB_COMPANY]

  def list(self):
    return [x for x in self.cir_db]

  def get(self, id):
    try:
      my_document = self.cir_db[id]
    except KeyError:
      api.abort(404, "Company {} not registered".format(id))
    return my_document

  def create(self, data):
    try:
      my_document = self.cir_db.create_document(data)
    except KeyError:
      api.abort(404, "Company {} already registered".format(id))
    return my_document

  def update(self, id, data):
    # Not currently supported
    return

  def delete(self, id):
    try:
      my_document = self.cir_db[id]
      my_document.delete()
    except KeyError:
      api.abort(404, "Company {} not registered".format(id))
    return
