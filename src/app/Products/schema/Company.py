from cloudant.query import Query
import time

from promise import Promise
from promise.dataloader import DataLoader

from app.helpers.dictionary import merge_values
from . import client, DB_COMPANY
# A Data Access Object to handle the reading and writing of Company records to the Cloudant DB


class CompanyDAO(DataLoader):
  def __init__(self):
    DataLoader.__init__(self)
    self.cir_db = client[DB_COMPANY]

  def list(self, filters: dict = {}):
    if len(filters.values()):
      return list(Query(self.cir_db, selector=filters).result)
    return [x for x in self.cir_db]

  def batch_load_fn(self, keys):
    return Promise.resolve([self.__get(id=key) for key in keys])

  def __get(self, id):
    try:
      my_document = self.cir_db[id]
    except KeyError:
      raise Exception(f'Empresa {id} no esta registrado')
    return my_document

  def create(self, data):
    try:
      my_document = self.cir_db.create_document(data)
    except KeyError:
      raise Exception(f'Empresa {id} ya esta registrado')
    return my_document

  def update(self, id, data):
    product = merge_values(self.get(id), data)
    product.save()
    return product

  def update_many(self, products: list, id_name: str = '_id'):
    for product in products:
      self.update(product[id_name], product)
      time.sleep(0.15)

  def delete(self, id: str):
    product = self.get(id)
    product.delete()
    return product
