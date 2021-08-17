from cloudant.query import Query

from . import client, DB_CERTIFIER
from app.helpers.dictionary import merge_values

# A Data Access Object to handle the reading and writing of Certifier records to the Cloudant DB


class CertifierDAO(object):
  def __init__(self):
    self.cir_db = client[DB_CERTIFIER]

  def list(self, filters: dict = {}):
    if len(filters.values()):
      return list(Query(self.cir_db, selector=filters).result)
    return [x for x in self.cir_db]

  def get(self, id):
    try:
      my_document = self.cir_db[id]
    except KeyError:
      raise Exception(f'Certificador {id} no esta registrado')
    return my_document

  def create(self, data):
    try:
      my_document = self.cir_db.create_document(data)
    except KeyError:
      raise Exception(f'Certificador {id} ya esta registrado')
    return my_document

  def update(self, id, data):
    product = merge_values(self.get(id), data)
    product.save()
    return product

  def delete(self, id: str):
    product = self.get(id)
    product.delete()
    return product
