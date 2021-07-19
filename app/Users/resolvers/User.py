from flask import request

from app.Users.schema.User import UserDAO
from app.Users.midleware import check_token

from . import query, user

user.set_alias('id', '_id')


@query.field("me")
@check_token()
def resolve_me(obj, info):
  return request.user_data
