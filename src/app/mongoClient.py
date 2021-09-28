from pymongo import MongoClient
from os import environ
import dns

mongoClient = MongoClient(environ.get('MONGO_URL'))
