from cloudant.client import Cloudant
from os import environ

client = Cloudant.iam(
    environ.get('DB_USERNAME'),
    environ.get('DB_API_KEY'),
    connect=True
)
