import time
from os import environ

from . import client, DB_USER


class UserDAO(object):
  def __init__(self):
    self.cir_db = client[DB_USER]

  def create_super_user(self):
    print("[User] Creating super user", flush=True)
    data = {
        'name': 'Sebastián',
        'lastName': 'Godínez',
        'email': 'sebastian.godinez@sansano.usm.cl',
        'firebaseId': environ.get('USER_ID'),
        'isAdmin': True,
    }
    # Have to rate limit it to less than 10 a second, due to free tier
    time.sleep(0.15)
    self.create(data)
    print("[User] complete", flush=True)

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
