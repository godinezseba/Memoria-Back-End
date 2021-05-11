import time
from os import environ

from app.api import api
from . import client, DB_USER

# A Data Access Object to handle the reading and writing of Product records to the Cloudant DB


class ProductDAO(object):
  def __init__(self):
    self.cir_db = client[DB_PRODUCT]

  def create(self, data):

    self.create(data)
