# Stub API Maker Served by Flask
It makes stub API based on under static folder structure and a setting file.


## Installation
I only tested in python3.6 yet.

```bash
$ pip install -r requirments.txt 
```

## Quickstart
I'll make an endpoint to be tested.

1\. Make a folder under static folder with method name.
- `mkdir -p static/mock/articles/GET`
- It will have endpoint, like `localhost:5000/articles/<FILENAME>/` 

2\. Add a response file under METHOD folder. 
- `echo '{"name": "urangurang", "age": 30}' > static/mock/articles/GET/1.json`
- You can get response `{"name": "urangurang", "age": 30}` from `localhost:5000/articles/1`.

3\. Add a setting file for response type, status code, etc.
- `touch static/mock/articles/response.yaml`
- You must make the `response.yaml`. Because this application makes a controller(view.py) when `response.yaml` exist under static folder. 
- It should be located in same level with method folder
- \- articles
     - GET
        - 1.json
        - 2.json
        - get.json
     - POST
     - *response.yaml* 

 
```bash
$ mkdir -p static/mock/articles/GET  # 1
$ echo '{"name": "urangurang", "age": 30}' > static/mock/articles/GET/1.json
$ touch static/mock/articles/response.yaml
$ python run.py

* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Check the result.
```bash
$ curl -X GET http://0.0.0.0:5000/articles/1
{"name": "urangurang", "age": 30}
```

## More things to do 

How to write `response.yaml` 
```yaml
METHOD:
  status_code: Every status codes supported in HTTP
  charset:
  mimetype:

```

`response.yaml` example 
```yaml
GET:
  status_code: 200
  charset: EUC-KR # If you use utf-8, you don't need to write 
  mimetype: text/html # If you use application/json, you don't need to write

POST:
  status_code: 404
  mimetype: application/javascript
```
