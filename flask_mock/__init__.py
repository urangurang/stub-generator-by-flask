# -*- coding:utf-8 -*-

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import flask_mock.views
import flask_mock.articles.views
import flask_mock.user_linkage_bicpoint.views


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
