from . import client, DB_CERTIFIER

# A Data Access Object to handle the reading and writing of Certifier records to the Cloudant DB


class CertifierDAO(object):
  def __init__(self):
    self.cir_db = client[DB_CERTIFIER]

  def list(self):
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
    # Not currently supported
    return

  def delete(self, id):
    try:
      my_document = self.cir_db[id]
      my_document.delete()
    except KeyError:
      raise Exception(f'Certificador {id} no existe')
    return