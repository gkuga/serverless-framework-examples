import json


def hello(event, context):
    name = event.get("queryStringParameters", {}).get("Name", "World!")
    body = {
        "message": f'Hello {name}',
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
