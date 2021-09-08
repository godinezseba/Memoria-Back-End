from bson.objectid import ObjectId

from app.helpers.dictionary import merge_values
from . import mongoDB

# A Data Access Object to handle the reading and writing of Certifier records to the Cloudant DB


class CertifierDAO(object):
  def __init__(self):
    self.colection = mongoDB['certifiers']

  def list(self, filters: dict = {}):
    if filters.get('ids'):
      filters['_id'] = {'$in': [ObjectId(id) for id in filters['ids']]}
      del filters['ids']
    return [x for x in self.colection.find(filters)]

  def get(self, id):
    my_document = self.colection.find_one({'_id': ObjectId(id)})
    if not my_document:
      raise Exception(f'Certificador {id} no esta registrado')
    return my_document

  def create(self, data):
    try:
      data['_id'] = self.colection.insert_one(data).inserted_id
    except KeyError:
      raise Exception(f'Error al crear la certificadora')
    return data

  def update(self, id, data):
    certifier = merge_values(self.get(id), data)
    self.colection.update_one({'_id': ObjectId(id)}, {'$set': certifier})
    return certifier

  def delete(self, id: str):
    certifier = self.get(id)
    self.colection.delete_one({'_id': ObjectId(id)})
    return certifier
