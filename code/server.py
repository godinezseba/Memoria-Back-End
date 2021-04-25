from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from model import api
from schema import *

api.init_app(app)

import route.Certifier
import route.Company
import route.Product

if __name__ == '__main__':
	app.run()
