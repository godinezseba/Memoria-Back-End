from flask import request
from functools import wraps
import requests

from app.api import api
from .schema.UserAppID import get_attributes


def check_token(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    token = request.headers.get('Authorization')
    if not token:
      api.abort(400, "No token provided.")

    # erros are treated in the schema
    response = get_attributes(token)
    request.user = response
    request.token = token
    return f(*args, **kwargs)
  return wrap
