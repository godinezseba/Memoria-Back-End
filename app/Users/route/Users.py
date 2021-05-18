from flask import request
from flask_restx import Resource

from app.api import api
from app.Users.midleware import check_token
from app.Users.model.User import UserModel

user_ns = api.namespace(
    'user', description='Users operations')


@user_ns.route('')
class User(Resource):
  @api.marshal_with(UserModel)
  @api.doc('Get current user information (if token is provided)')
  @check_token()
  def get(self):
    return request.user_data
