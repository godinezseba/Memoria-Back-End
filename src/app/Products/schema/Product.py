from bson.objectid import ObjectId

from app.helpers.dictionary import merge_values
from . import mongoDB


class ProductDAO(object):
  # A Data Access Object to handle the reading and writing of Product records to the Cloudant DB
  def __init__(self):
    self.colection = mongoDB['products']

  def list(self, filters: dict = {}, sort: list = []):
    if filters.get('barCode'):
      filters['barCode'] = int(filters['barCode'])
    if filters.get('ids'):
      filters['_id'] = {'$in': [ObjectId(id) for id in filters['ids']]}
      del filters['ids']
    if len(sort) == 2:
      return [x for x in self.colection.find(filters).sort(sort[0], sort[1])]
    return [x for x in self.colection.find(filters)]

  def get(self, id: str):
    my_document = self.colection.find_one({'_id': ObjectId(id)})
    if not my_document:
      raise Exception(f'Producto {id} no esta registrado')
    return my_document

  def create(self, data: dict):
    try:
      data['_id'] = self.colection.insert_one(data).inserted_id
    except Exception as e:
      print(e, flush=True)
      raise Exception(f'Error al guardar el producto')
    return data

  def create_many(self, products: list):
    self.colection.insert_many(products)

  def update(self, id, data):
    product = merge_values(self.get(id), data)
    self.colection.update_one({'_id': ObjectId(id)}, {'$set': product})
    return product

  def update_many(self, products: list, id_name: str = '_id'):
    for product in products:
      self.update(product[id_name], product)

  def delete(self, id: str):
    product = self.get(id)
    self.colection.delete_one({'_id': ObjectId(id)})
    return product
