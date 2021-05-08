from flask_restx import fields

from code.api import api

UserModel = api.model('User', {
    'name': fields.String(required=True, description='The name of the user'),
    'email': fields.String(required=True, description='The email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'lastName': fields.String(description='The last name of the user'),
    'token': fields.String(description='The temporal token for this user'),
    'googleId': fields.String(description='The ID that save Google for this user'),
    'isAdmin': fields.Boolean(description='A condition to know if the user has all the access'),
    'companies': fields.List(fields.Integer(description='Companies that can be edited by the user')),
    'certifiers': fields.List(fields.Integer(description='Certifiers that can be edited by the user')),
})
