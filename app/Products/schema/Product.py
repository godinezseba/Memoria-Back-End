import csv
import time

from app.api import api
from . import client, DB_PRODUCT

# A Data Access Object to handle the reading and writing of Product records to the Cloudant DB


class ProductDAO(object):
  def __init__(self):
    self.cir_db = client[DB_PRODUCT]

  def import_data(self):
    print("Importing dummy data", end='', flush=True)
    with open('product.dummy.txt') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count > 0:
          data = {
              'barcode_id': row[4],
              'type': row[0],
              'category': row[2],
              'model': row[3],
              'brand': row[1],
              'rating_data': {
                  'efficiency': int(row[6]),
                  'energy': float(row[7]) + float(row[8]),
                  'CO2': float(row[13]),
                  'otherGG': float(row[14]),
                  'water': float(row[11]),
                  'plastic': float(row[9]),
                  'lifetime': float(row[10]),
                  'recyclability': int(row[12]),
                  'repairability': int(row[15])
              }
          }
          # Have to rate limit it to less than 10 a second, due to free tier
          time.sleep(0.15)
          self.create(data)
          print(".", end='', flush=True)
        line_count += 1
    print("complete")

  def list(self):
    return [x for x in self.cir_db]

  def get(self, id):
    try:
      my_document = self.cir_db[id]
      my_document['id'] = my_document['barcode_id']
    except KeyError:
      api.abort(404, "Product {} not registered".format(id))
    return my_document

  def get_by_barcode(self, barcode_id):
    # For now this is easy, since id is the same as barcode_id....in the future this would need an
    # index of some such search ability
    try:
      my_document = self.cir_db[barcode_id]
      my_document['id'] = my_document['barcode_id']
    except KeyError:
      api.abort(404, "Product {} not registered".format(id))
    return my_document

  def create(self, data):
    # For now, we'll set the id to be the same as the barcode_id. For production systems, we would
    # probably want these seperate, and to implement indexed searching by barcode_id for GET.
    try:
      data['_id'] = data['barcode_id']
      my_document = self.cir_db.create_document(data)
      my_document['id'] = my_document['barcode_id']
    except KeyError:
      api.abort(404, "Product {} already registered".format(id))
    return my_document

  def update(self, id, data):
    # Not currently supported
    return

  def delete(self, id):
    try:
      my_document = self.cir_db[id]
      my_document.delete()
    except KeyError:
      api.abort(404, "Product {} not registered".format(id))
    return
