import json


def about(event, context):
    body = {
        "Service Name": "S3upload",
        "Developend by": "Sukanto Mondal"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def upload(event, context):    
    response = {
        "statusCode": 200,
        "body": "Uploaded successfully"
    }

    return response 
