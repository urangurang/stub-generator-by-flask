import os
from pathlib import Path

ROOT_PATH = os.getcwd()

STATIC_PATH = "static/mock"

IMPORT_PATH = """from flask import Response, request
from flask_mock import app

"""

DEF_FORMAT = """
@app.route("{0}/<filename>/", methods={1})
@app.route("{0}", methods={1})
def {2}(filename):
    res = Response() 
    res.mimetype = "application/json"
    body = ""
    if request.method == "GET":
        with open('{3}{4}/GET/' + filename + '.json') as f:
            body = f.read()
    elif request.method == "POST":
        with open('{3}{4}/POST/post.json') as f:
            pass
    elif request.method == "PUT":
        with open('{3}{4}/PUT/put.json') as f:
            pass
    elif request.method == "DELETE":
        with open('{3}{4}/DELETE/delete/json') as f:
            pass
    res.data = body
    return res
"""

INIT_FORMAT = """# -*- coding:utf-8 -*-

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import flask_mock.views
{0}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
"""

will_be_imported_views = []
CURRENT_PATH = os.getcwd()

for root, methods, files in os.walk(STATIC_PATH):
    if 'response.yaml' in files:
        route = root.replace(STATIC_PATH, "")
        package = route.replace("/", "_")[1:]
        DEF = DEF_FORMAT.format(route, methods.__str__(), package, STATIC_PATH, route)
        folder = "flask_mock/{}".format(package)
        try:
            os.mkdir(folder, 0o755)
        except:
            pass
        os.chdir(CURRENT_PATH + "/flask_mock/" + package)
        Path("__init__.py").touch()
        with open("views.py", "w") as f:
            f.write(IMPORT_PATH)
            f.write(DEF)
        os.chdir(ROOT_PATH)
        will_be_imported_views.append("import flask_mock.{}.views".format(package))

with open(CURRENT_PATH + "/flask_mock/__init__.py", "w") as f:
    f.write(INIT_FORMAT.format("\n".join(will_be_imported_views)))




