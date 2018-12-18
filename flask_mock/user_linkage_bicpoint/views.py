from flask import request, send_from_directory
from flask_mock import app


@app.route("/user/linkage/bicpoint", methods=['POST'])
def user_linkage_bicpoint():
    if request.method == "GET":
        with open('static/mock/user/linkage/bicpoint/GET') as f:
            pass
    elif request.method == "POST":
        with open('static/mock/user/linkage/bicpoint/POST') as f:
            pass
    elif request.method == "PUT":
        with open('static/mock/user/linkage/bicpoint/PUT') as f:
            pass
    elif request.method == "DELETE":
        with open('static/mock/user/linkage/bicpoint/DELETE') as f:
            pass
