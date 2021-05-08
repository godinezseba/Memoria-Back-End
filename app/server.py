from flask import Flask
from flask_cors import CORS

from flask_jwt_extended import JWTManager

from os import environ

from .api import api
from .Products.schema import *
from .Users.route import *
from .Products.route import *

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
CORS(app)

api.init_app(app)

if __name__ == '__main__':
  app.run()
