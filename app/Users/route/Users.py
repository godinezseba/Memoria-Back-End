from flask import request
from flask_restx import Resource

from app.api import api
from app.Users.schema.UserAppID import get_information
from app.Users.midleware import check_token

user_ns = api.namespace(
    'user', description='Users operations')


@user_ns.route('')
class User(Resource):
  # @api.doc('List products')
  # @api.doc(params={'barcode_id': 'The barcode ID of this product (optional)'})
  @check_token
  def get(self):
    token = request.token
    return get_information(token)

  @check_token
  def post(self):
    print(api.payload, flush=True)
    print(request.user['credentials']['companies'], flush=True)
