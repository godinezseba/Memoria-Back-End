from flask_restx import Resource, reqparse
from flask_jwt_extended import jwt_required

from app.api import api
from app.Products.model.Company import CompanyModel
from app.Products.schema.Company import CompanyDAO

company_ns = api.namespace(
    'company', description='User CIR Company Operations')


@company_ns.route('')
class Company(Resource):
  @api.marshal_with(CompanyModel)
  @api.doc('List companies')
  def get(self):
    return CompanyDAO().list()

  @api.marshal_with(CompanyModel, code=201)
  @api.doc(body=CompanyModel)
  @jwt_required()
  def post(self):
    return CompanyDAO().create(api.payload), 201


@company_ns.route('/<string:id>')
class CompanyWithID(Resource):
  @api.marshal_with(CompanyModel)
  @api.doc(params={'id': 'The unique ID of this company'})
  def get(self, id):
    return CompanyDAO().get(id)

  @api.marshal_with(CompanyModel)
  @api.doc(params={'id': 'The unique ID of this company'})
  @jwt_required()
  def delete(self, id):
    return CompanyDAO().delete(id)