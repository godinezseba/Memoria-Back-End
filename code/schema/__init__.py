from cloudant.client import Cloudant

# You must overwrite the values in api_access below with those from your service credential, that you created in IBM Cloud IAM for Cloudant.
# The actual values below are to just show the format - and these are no longer valid.
api_access = {
  "apikey": "zsumbYQJoRR6BuE3aGnymYn-aJ19-vNKvxlXLhEmUyX8",
  "host": "880e7909-b0bf-4f0f-af54-529d907689bd-bluemix.cloudantnosqldb.appdomain.cloud",
  "iam_apikey_description": "Auto-generated for key 6a9e43cf-ac67-412a-ba57-6d4186ec01cf",
  "iam_apikey_name": "Credenciales de servicio-1",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/f3503acd3662479f95e59aefe3026dcc::serviceid:ServiceId-3d2bb378-676a-4fab-b6b6-10b55b27a69f",
  "url": "https://880e7909-b0bf-4f0f-af54-529d907689bd-bluemix.cloudantnosqldb.appdomain.cloud",
  "username": "880e7909-b0bf-4f0f-af54-529d907689bd-bluemix"
}

client = Cloudant.iam(
  api_access['username'],
  api_access['apikey'],
  connect=True
)

# name of the dbs used in the proyect

DB_PRODUCT = 'cir-db-product'
DB_CERTIFIER = 'cir-db-certifier'


if not DB_CERTIFIER in client.all_dbs():
  client.create_database(DB_CERTIFIER)


if not DB_PRODUCT in client.all_dbs():
  client.create_database(DB_PRODUCT)

  from .Product import ProductDAO

  try:
    ProductDAO().import_data()
  except Exception as e:
    print('Error while creating dummy data!', flush=True)
    print(e, flush=True)
