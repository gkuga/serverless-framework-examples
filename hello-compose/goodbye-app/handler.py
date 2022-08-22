import json
import os


def goodbye(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
        "helloAppAPIURL": os.environ.get('HELLO_API_URL'),
        "envTest": os.environ.get('ENV_TEST'),
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
