from flask import Flask
from flask_cors import CORS

from .api import api
from .Users.route import *
from .Products.route import *

app = Flask(__name__)
CORS(app)

api.init_app(app)

if __name__ == '__main__':
  app.run()
