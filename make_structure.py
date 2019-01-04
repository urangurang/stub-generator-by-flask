import os
from pathlib import Path


ROOT_PATH = os.getcwd()
STATIC_PATH = "static/mock"
IMPORT_PATH = """import yaml
from flask import Response, request
from flask_mock import app

"""
INIT_FORMAT = """# -*- coding:utf-8 -*-

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

import flask_mock.views
{0}

"""
DEF_FORMAT = """
@app.route("{0}/<filename>/", methods={1})
@app.route("{0}/", methods={1})
def {2}(filename=None):
    with open('{3}{4}/response.yaml') as f:
        res_property = yaml.load(f)
    
    res = Response() 
    try: 
        res.status_code = res_property[request.method]["status_code"]
    except KeyError:
        res.status_code = 200
    
    try:
        res.mimetype = res_property[request.method]["mimetype"]
    except KeyError:
        res.mimetype = "application/json"
        
    if request.method == "GET":
        if filename is None:
            with open('{3}{4}/GET/get.json') as f:
                res.data = f.read()
        else:
            with open('{3}{4}/GET/' + filename + '.json') as f:
                res.data = f.read()
    elif request.method == "POST":
        with open('{3}{4}/POST/post.json') as f:
            pass
            
    return res
"""
will_be_imported_views = []
CURRENT_PATH = os.getcwd()


def create_stub_views():
    for root, methods, files in os.walk(STATIC_PATH):
        if 'response.yaml' in files:
            route = root.replace(STATIC_PATH, "")
            package = route.replace("/", "_")[1:]
            DEF = DEF_FORMAT.format(route,
                                    methods.__str__(),
                                    package,
                                    STATIC_PATH,
                                    route)
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
            will_be_imported_views.append("import flask_mock.{}.views"
                                          .format(package))

    with open(CURRENT_PATH + "/flask_mock/__init__.py", "w") as f:
        f.write(INIT_FORMAT.format("\n".join(will_be_imported_views)))


if __name__ == "__main__":
    create_stub_views()
