from flask_restx import fields

from app.api import api

ActionsModel = api.model('Actions', {
    '_id': fields.String(readonly=True, description='The unique actions registration identifier'),
    'name': fields.String(readonly=True, description='The name of the file'),
    'file': fields.String(required=True, description='The file of the actions in base64'),
    'description': fields.String(description='A description of the action'),
    'companyType': fields.String(description='The type of company that update this file'),
    'companyId': fields.String(description='The id of the company/certifier that create this report'),
})
