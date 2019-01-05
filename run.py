# -*- coding: utf-8 -*-

from flask_stub import app
from utils import make_views_by_static

if __name__ == '__main__':
    make_views_by_static()
    app.run(host='0.0.0.0', debug=True, port=5000)
