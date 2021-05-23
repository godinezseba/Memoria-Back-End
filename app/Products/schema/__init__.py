from app.cloudantClient import client

# name of the dbs used in the proyect

DB_CERTIFIER = 'cir-db-certifier'
DB_COMPANY = 'cir-db-company'
DB_PRODUCT = 'cir-db-product'


if not DB_CERTIFIER in client.all_dbs():
  client.create_database(DB_CERTIFIER)

if not DB_COMPANY in client.all_dbs():
  client.create_database(DB_COMPANY)

if not DB_PRODUCT in client.all_dbs():
  client.create_database(DB_PRODUCT)

  from .Product import ProductDAO

  try:
    ProductDAO().import_data()
  except Exception as e:
    print('Error while creating dummy data!', flush=True)
    print(e, flush=True)
