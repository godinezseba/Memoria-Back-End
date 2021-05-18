from app.cloudantClient import client

# name of the dbs used in the proyect

DB_USER = 'cir-db-user'

if not DB_USER in client.all_dbs():
  client.create_database(DB_USER)

  from .User import UserDAO

  try:
    UserDAO().create_super_user()
  except Exception as e:
    print('[User] Error while creating dummy data!', flush=True)
    print(e, flush=True)
