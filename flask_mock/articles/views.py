from flask import send_from_directory, Response
from flask_mock import app

STATIC_PATH = "static/mock/"
DETAIL_PATH = "articles/"
BIC_POINT = "/user/linkage/bicpoint"


@app.route("/d")
def wad():
    return "!@#@!#"


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
    return send_from_directory(STATIC_PATH + DETAIL_PATH, "articles.json")


