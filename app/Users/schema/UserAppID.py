import requests
from app.api import api

__regionPath = f'https://us-south'
__tenantId = '463ecc77-cba1-432f-a5ac-a62a9e795cca'


def get_attributes(token):
  try:
    headers = {'Authorization': token}
    response = requests.get(
        f'{__regionPath}.appid.cloud.ibm.com/api/v1/attributes', headers=headers)
  except Exception as e:
    print(e, flush=True)
    api.abort(401, "Invalid token.")

  return response.json()


def get_information(token):
  try:
    headers = {'Authorization': token}
    response = requests.get(
        f'{__regionPath}.appid.cloud.ibm.com/oauth/v4/{__tenantId}/userinfo', headers=headers)
  except Exception as e:
    print(e, flush=True)
    api.abort(401, "Invalid token.")

  return response.json()

# def get_users(token)
