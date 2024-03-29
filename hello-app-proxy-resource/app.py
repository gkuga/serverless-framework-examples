import json

from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext

app = APIGatewayRestResolver()


@app.get("/")
def index():
    return {"hello": "world"}


@app.get("/hello")
def hello():
    name: str = app.current_event.get_query_string_value(
        name="name", default_value="")
    body = {
        "message": f'Hello {name}',
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


@app.get("/api/<id>")
def apiid(id: str):
    body = {
        'message': 'API path',
        'id': id,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


@app.get("/api/<id>/temp")
def api():
    body = {
        "message": 'API path',
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
