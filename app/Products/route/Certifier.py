from flask_restx import Resource

from app.api import api
from app.Products.model.Certifier import CertifierModel
from app.Products.schema.Certifier import CertifierDAO
from app.Users.midleware import check_token

certifier_ns = api.namespace(
    'certifier', description='User CIR Certifier Operations')


@certifier_ns.route('')
class Certifier(Resource):
  @api.marshal_with(CertifierModel)
  @api.doc('List certifiers')
  def get(self):
    return CertifierDAO().list()

  @api.marshal_with(CertifierModel, code=201)
  @api.doc(body=CertifierModel)
  @check_token(check_admin=True)
  def post(self):
    return CertifierDAO().create(api.payload), 201


@certifier_ns.route('/<string:id>')
class CertifierWithID(Resource):
  @api.marshal_with(CertifierModel)
  @api.doc(params={'id': 'The unique ID of this certifier'})
  def get(self, id):
    return CertifierDAO().get(id)

  @api.marshal_with(CertifierModel)
  @api.doc(params={'id': 'The unique ID of this certifier'})
  @check_token(check_admin=True)
  def delete(self, id):
    return CertifierDAO().delete(id)
