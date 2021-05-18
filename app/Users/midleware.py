from flask import request
from functools import wraps
from firebase_admin import auth

from app.api import api
from app.firebaseClient import firebase_client
from .schema.User import UserDAO


def check_token(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    token = request.headers.get('Authorization')
    if not token:
      api.abort(400, "No token provided.")

    try:
      user = auth.verify_id_token(token, app=firebase_client)
    except Exception as e:
      print('[Midleware]', end='', flush=True)
      print(e, flush=True)
      api.abort(403)

    # erros are treated in the schema
    user_data = UserDAO().get(user['uid'])

    request.user = user
    request.token = token
    request.user_data = user_data
    return f(*args, **kwargs)
  return wrap
