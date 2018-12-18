from flask import request, send_from_directory
from flask_mock import app


@app.route("/articles", methods=['POST', 'GET'])
def articles():
    if request.method == "GET":
        print("/articles GET")
        with open('static/mock/articles/GET') as f:
            pass
    elif request.method == "POST":
        with open('static/mock/articles/POST') as f:
            pass
    elif request.method == "PUT":
        with open('static/mock/articles/PUT') as f:
            pass
    elif request.method == "DELETE":
        with open('static/mock/articles/DELETE') as f:
            pass
