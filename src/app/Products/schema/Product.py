from cloudant.query import Query
import time

from app.helpers.dictionary import merge_values

from . import client, DB_PRODUCT

# A Data Access Object to handle the reading and writing of Product records to the Cloudant DB


class ProductDAO(object):
  def __init__(self):
    self.cir_db = client[DB_PRODUCT]

  def list(self, filters: dict = {}, sort: list = []):
    if len(filters.values()):
      if filters.get('barCode'):
        filters['barCode'] = int(filters['barCode'])
      if filters.get('ids'):
        filters['_id'] = {'$in': filters['ids']}
        del filters['ids']
      return list(Query(self.cir_db, selector=filters).result)
    return [x for x in self.cir_db]

  def get(self, id: str):
    try:
      my_document = self.cir_db[id]
    except KeyError:
      raise Exception(f'Producto {id} no esta registrado')
    return my_document

  def create(self, data: dict):
    try:
      my_document = self.cir_db.create_document(data)
    except KeyError:
      raise Exception(f'Producto {data["barCode"]} ya esta registrado')
    return my_document

  def create_many(self, products: list):
    for product in products:
      self.create(product)
      time.sleep(0.15)

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
