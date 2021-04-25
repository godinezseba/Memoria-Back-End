from flask_restx import Resource, reqparse

from model import api
from model.Company import CompanyModel
from schema.Company import CompanyDAO

company_ns = api.namespace('company', description='User CIR Company Operations')

@company_ns.route('')
class Company(Resource):
  @api.marshal_with(CompanyModel)
  @api.doc('List companys')
  def get(self):
    return CompanyDAO().list()

  @api.marshal_with(CompanyModel, code=201)
  @api.doc(body=CompanyModel)
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
  def delete(self, id):
    return CompanyDAO().delete(id)
