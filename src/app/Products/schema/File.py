from bson.objectid import ObjectId
from promise import Promise
from promise.dataloader import DataLoader

from app.helpers.dictionary import merge_values
from . import mongoDB


class FileDAO(DataLoader):
  # A Data Access Object to handle the reading and writing of File records to the Cloudant DB
  def __init__(self):
    DataLoader.__init__(self)
    self.colection = mongoDB['files']

  def list(self, filters: dict = {}):
    if filters.get('ids'):
      filters['_id'] = {'$in': [ObjectId(id) for id in filters['ids']]}
      del filters['ids']
    return [x for x in self.colection.find(filters)]

  def batch_load_fn(self, keys):
    return Promise.resolve(self.list(filters={'ids': keys}))

  def get_one(self, id: str):
    my_document = self.colection.find_one({'_id': ObjectId(id)})
    if not my_document:
      raise Exception(f'Archivo {id} no esta registrado')
    return my_document

  def create(self, data):
    try:
      data['_id'] = self.colection.insert_one(data).inserted_id
    except Exception as e:
      print(e, flush=True)
      raise Exception('Error al crear el archivo')
    return data

  def create_many(self, files: list):
    if len(files):
      my_ids = self.colection.insert_many(files).inserted_ids
      return my_ids
    return []

  def update(self, id, data):
    file = merge_values(self.get_one(id), data)
    self.colection.update_one({'_id': ObjectId(id)}, {'$set': file})
    return file

  def delete(self, id: str):
    file = self.get_one(id)
    self.colection.delete_one({'_id': ObjectId(id)})
    return file
