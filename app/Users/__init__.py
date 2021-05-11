from cloudant.client import Cloudant
from os import environ

client = Cloudant.iam(
    environ.get('DB_USERNAME'),
    environ.get('DB_API_KEY'),
    connect=True
)

# name of the dbs used in the proyect

DB_USER = 'cir-db-user'

if not DB_USER in client.all_dbs():
  client.create_database(DB_USER)

  from .USER import UserDAO

  try:
    print("Creating super user", flush=True)
    super_user = {
        'name': environ.get('USER_NAME'),
        'email': environ.get('USER_EMAIL'),
        'password': environ.get('USER_PASSWORD'),
    }
    UserDAO().create(super_user)
  except Exception as e:
    print('Error while creating dummy data!', flush=True)
    print(e, flush=True)
