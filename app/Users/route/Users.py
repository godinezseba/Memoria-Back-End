from flask import request
from flask_restx import Resource

from firebase_admin import auth

from app.api import api
from app.firebaseClient import firebase_client
from app.Users.midleware import check_token
from app.Users.model.User import UserModel
from app.Users.schema.User import UserDAO

user_ns = api.namespace(
    'user', description='Users operations')


@user_ns.route('')
class User(Resource):
  @api.marshal_with(UserModel)
  @api.doc('Deprecated: Get current user information (if token is provided)')
  @check_token()
  def get(self):
    # Deprecated
    return request.user_data

  @api.marshal_with(UserModel)
  @api.doc('Create new user (if admin token is provided)')
  @check_token(check_admin=True)
  def post(self):
    # first, try create user in firebase
    try:
      new_user_data = api.payload
      firebase_user = auth.create_user(
          email=new_user_data['email'],
          password='memoria123',  # TODO generate random pasword
          email_verified=True,
          app=firebase_client
      )
      new_user_data['firebaseId'] = firebase_user.uid
    except Exception as e:
      print('[creating User]', end=' ', flush=True)
      print(e, flush=True)
      api.abort(502, 'Error creating value in Firebase')
    # second, try creating user here
    try:
      new_user = UserDAO().create(new_user_data)
    except Exception as e:
      print('[creating User]', end=' ', flush=True)
      print(e, flush=True)
      auth.delete_user(firebase_user.uid)
      api.abort(404, "Error creating the user")
    return new_user, 201
