from flask_restx import fields

from app.api import api

UserModel = api.model('User', {
    'name': fields.String(required=True, description='The name of the user'),
    'lastName': fields.String(description='The last name of the user'),
    'email': fields.String(required=True, description='The email of the user'),
    'firebaseId': fields.String(description='The ID that save Firebase for this user'),
    'isAdmin': fields.Boolean(description='A condition to know if the user has all the access'),
    'companyType': fields.String(description='The type of company where this user works'),
    'companyId': fields.String(description='The company where this user works'),
    'editableCompanies': fields.List(fields.Integer(description='Companies that can be edited by the user')),
})
