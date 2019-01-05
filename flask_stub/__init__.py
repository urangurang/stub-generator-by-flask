# -*- coding:utf-8 -*-

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

import flask_stub.views

