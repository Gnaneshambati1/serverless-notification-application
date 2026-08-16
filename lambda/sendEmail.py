import boto3
import json

ses = boto3.client(
    "ses",
    region_name="ap-south-1"
)


def lambda_handler(event, context):

    sender = "gnaneshambati77@gmail.com"
    recipient = "gnaneshambati7@gmail.com"

    subject = event.get(
        "subject",
        "Serverless Sending Application"
    )

    message = event.get(
        "message",
        "Hello from AWS Lambda and Amazon SES!"
    )

    response = ses.send_email(
        Source=sender,
        Destination={
            "ToAddresses": [
                recipient
            ]
        },
        Message={
            "Subject": {
                "Data": subject,
                "Charset": "UTF-8"
            },
            "Body": {
                "Text": {
                    "Data": message,
                    "Charset": "UTF-8"
                }
            }
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Email sent successfully",
            "messageId": response["MessageId"]
        })
    }