from flask import request
from functools import wraps
from firebase_admin import auth

from app.firebaseClient import firebase_client
from app.Users.schema.User import UserDAO


def check_token(check_admin: bool = False, raise_on_null: bool = True):
  def inner_function(f):
    @wraps(f)
    def wrap(*args, **kwargs):
      token = request.headers.get('Authorization')
      if not token:
        if raise_on_null:
          raise Exception('Necesita permisos')
        return f(*args, **kwargs)
      try:
        user = auth.verify_id_token(token, app=firebase_client)
      except Exception as e:
        print('[Midleware]', end=' ', flush=True)
        print(e, flush=True)
        raise Exception('Necesita permisos')

      # erros are treated in the schema
      user_data = UserDAO().get(user['uid'])

      if check_admin and not user_data.get('isAdmin', False):
        raise Exception('Solo administradores pueden acceder')

      request.user = user
      request.token = token
      request.user_data = user_data
      return f(*args, **kwargs)
    return wrap
  return inner_function
