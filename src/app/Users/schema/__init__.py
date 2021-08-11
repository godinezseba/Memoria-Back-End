from app.cloudantClient import client

# name of the dbs used in the proyect

DB_USER = 'cir-db-user'

if not DB_USER in client.all_dbs():
  client.create_database(DB_USER)
