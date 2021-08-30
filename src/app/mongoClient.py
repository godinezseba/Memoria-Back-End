from pymongo import MongoClient
from os import environ
import dns

mongo_credentials = {
    'host': environ.get('MONGO_HOST'),
    'db': environ.get('MONGO_DB'),
    'user': environ.get('MONGO_USER'),
    'pass': environ.get('MONGO_PASS'),
}
mongoUrl = "mongodb+srv://{user}:{pass}@{host}/{db}?retryWrites=true&w=majority".format(
    **mongo_credentials)
mongoClient = MongoClient(mongoUrl)
