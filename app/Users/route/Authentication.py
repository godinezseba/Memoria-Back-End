from flask_restx import Resource
from flask_jwt_extended import create_access_token

from app.api import api

auth_ns = api.namespace(
    'auth', description='Authentication methods')


@auth_ns.route('/email')
class Auth(Resource):
  @api.doc('Login system with email and password')
  def post(self):
    email = api.payload['email']
    password = api.payload['password']
    if email != "test" or password != "test":
      return {"msg": "Bad username or password"}, 401

    access_token = create_access_token(identity=email)
    return {'access_token': access_token}
