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
$ echo '{"name": "urangurang", "age": 30}' > articles/GET/1.json
$ touch articles/response.yaml
$ cd ../..
$ python make_structure.py
$ python run.py

* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Check the result.
```bash
$ curl -X GET http://0.0.0.0:5000/articles/1
{"name": "urangurang", "age": 30}
```

`response.yaml` 

```yaml
GET:
  status_code: 200
  charset: utf-16 # If you use utf-8, you don't need to write 
  mimetype: text/html # If you use application/json, you don't need to write

POST:
  status_code: 404
  mimetype: text/html
```
