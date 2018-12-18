# -*- coding:utf-8 -*-

import json

from flask import Flask, send_from_directory, Response
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

STATIC_PATH = "static/mock/"
DETAIL_PATH = "articles/"
BIC_POINT = "/user/linkage/bicpoint"


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route(BIC_POINT, methods=['GET', 'POST'])
def cancel_card():
    with open(STATIC_PATH + BIC_POINT + "/post.json") as f:
        data = f.read()
    res = Response()
    res.set_data(data)
    res.status_code = 200
    res.mimetype = 'application/json'
    return res


@app.route("/articles/")
def articles():
    print("!!!!")
    return send_from_directory(STATIC_PATH + DETAIL_PATH, "all.json")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)