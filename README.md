# API stub maker served by Flask

## Installation
Only tested in python3.6
```bash
$ pip install -r requirments.txt 
```

## Quickstart
Make an endpoint you want to use.
 
```bash
$ cd static/mock
$ mkdir -p articles/GET
$ touch articles/GET/1.json
$ echo '{"name": "urangurang"}' > articles/GET/1.json
$ touch articles/response.yaml
$ cd ../..
$ python make_structure.py
$ python run.py

* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Check the result.
```bash
$ curl -X GET http://0.0.0.0:5000/articles/1
{"name": "urangurang"}
```
