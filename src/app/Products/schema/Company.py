from bson.objectid import ObjectId
from promise import Promise
from promise.dataloader import DataLoader

from app.helpers.dictionary import merge_values
from . import mongoDB


class CompanyDAO(DataLoader):
  # A Data Access Object to handle the reading and writing of Company records to the Cloudant DB
  def __init__(self):
    DataLoader.__init__(self)
    self.colection = mongoDB['companies']

  def list(self, filters: dict = {}):
    if filters.get('ids'):
      filters['_id'] = {'$in': [ObjectId(id) for id in filters['ids']]}
      del filters['ids']
    return [x for x in self.colection.find(filters)]

  def batch_load_fn(self, keys):
    return Promise.resolve(self.list(filter={'ids': keys}))

  def __get(self, id: str):
    my_document = self.colection.find_one({'_id': ObjectId(id)})
    if not my_document:
      raise Exception(f'Empresa {id} no esta registrado')
    return my_document

  def create(self, data):
    try:
      data['_id'] = self.colection.insert_one(data).inserted_id
    except Exception as e:
      print(e, flush=True)
      raise Exception(f'Empresa {id} ya esta registrado')
    return data

  def update(self, id, data):
    company = merge_values(self.get(id), data)
    self.colection.update_one({'_id': ObjectId(id)}, {'$set': company})
    return company

  def update_many(self, companies: list, id_name: str = '_id'):
    for company in companies:
      self.update(company[id_name], company)

  def delete(self, id: str):
    company = self.__get(id)
    self.colection.delete_one({'_id': ObjectId(id)})
    return company
