import json

from chalice import Chalice

app = Chalice(app_name="helloworld")


@app.route("/")
def index():
    return {"hello": "world"}


@app.route("/hello")
def hello(event, context):
    name = event.get("queryStringParameters", {}).get("Name", "World!")
    body = {
        "message": f'Hello {name}',
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


@app.route("/goodbye")
def goodbye(event, context):
    body = {
        "message": 'Good-bye',
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


@app.route("/api/{proxy+}")
def api(event, context):
    body = {
        "message": 'API path',
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


@app.on_s3_event(bucket='my-bucket-test-12345')
def handler(event):
    print("Object uploaded for bucket: %s, key: %s"
          % (event.bucket, event.key))
