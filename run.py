# -*- coding: utf-8 -*-

from flask_mock import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
