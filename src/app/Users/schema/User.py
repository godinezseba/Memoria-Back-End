from . import client, DB_USER


class UserDAO(object):
  def __init__(self):
    self.cir_db = client[DB_USER]

  # this method must be called after the user is created in
  # firebase, becase the firebase uid is used as id
  def create(self, data):
    data['_id'] = data['firebaseId']
    my_document = self.cir_db.create_document(data)

    return my_document

  def get(self, id):
    try:
      my_document = self.cir_db[id]
    except KeyError:
      raise Exception(f'Usuario {id} no esta registrado')
    return my_document
