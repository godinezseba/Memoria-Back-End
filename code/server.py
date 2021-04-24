import csv
import time

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from model import api

api.init_app(app)

import route.Product

if __name__ == '__main__':
	app.run()
