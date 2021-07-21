from . import client, DB_PRODUCT

# A Data Access Object to handle the reading and writing of Product records to the Cloudant DB


class ProductDAO(object):
  def __init__(self):
    self.cir_db = client[DB_PRODUCT]

  def list(self):
    return [x for x in self.cir_db]

  def get(self, id):
    try:
      my_document = self.cir_db[id]
    except KeyError:
      raise Exception(f'Producto {id} no esta registrado')
    return my_document

  def get_by_barcode(self, barcode_id):
    # For now this is easy, since id is the same as barcode_id....in the future this would need an
    # index of some such search ability
    try:
      my_document = self.cir_db[barcode_id]
      my_document['id'] = my_document['barCode']
    except KeyError:
      raise Exception(f'Producto {id} no esta registrado')
    return my_document

  def create(self, data):
    # For now, we'll set the id to be the same as the barcode_id. For production systems, we would
    # probably want these seperate, and to implement indexed searching by barcode_id for GET.
    try:
      data['_id'] = str(data['barCode'])
      my_document = self.cir_db.create_document(data)
    except KeyError:
      raise Exception(f'Producto {id} ya esta registrado')
    return my_document

  def update(self, id, data):
    # Not currently supported
    return

  def delete(self, id):
    try:
      my_document = self.cir_db[id]
      my_document.delete()
    except KeyError:
      raise Exception(f'Producto {id} no existe')
    return
