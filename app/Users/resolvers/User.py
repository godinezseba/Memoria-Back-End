from flask import request

from firebase_admin import auth

from app.firebaseClient import firebase_client
from app.Users.schema.User import UserDAO
from app.Users.midleware import check_token

from . import query, mutation, user

user.set_alias('id', '_id')


@query.field('me')
@check_token()
def resolve_me(obj, info):
  return request.user_data


@mutation.field('createUser')
@check_token(check_admin=True)
def resolve_create(obj, info, values):
  # first, try create user in firebase
  try:
    firebase_user = auth.create_user(
        email=values['email'],
        password='memoria123',  # TODO generate random pasword
        email_verified=True,
        app=firebase_client
    )
    values['firebaseId'] = firebase_user.uid
  except Exception as e:
    print('[creating User]', end=' ', flush=True)
    print(e, flush=True)
    raise Exception('Error al crear el usuario en Firebase')
  # second, try creating user here
  try:
    new_user = UserDAO().create(values)
  except Exception as e:
    print('[creating User]', end=' ', flush=True)
    print(e, flush=True)
    auth.delete_user(firebase_user.uid)
    raise Exception('Error creando el usuario')
  return new_user
