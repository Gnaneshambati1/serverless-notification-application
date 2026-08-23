import os
import json
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ses = boto3.client("ses", region_name=os.environ.get("AWS_REGION", "ap-south-1"))
SENDER = os.environ["SENDER_EMAIL"]  # injected via Lambda environment variables


def lambda_handler(event, context):
    recipient = event.get("email")
    subject = event.get("subject", "Serverless Notification")
    message = event.get("message", "Hello from AWS Lambda and Amazon SES!")

    if not recipient:
        logger.warning("Request missing required field 'email'")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing required field: 'email'"})
        }

    try:
        response = ses.send_email(
            Source=SENDER,
            Destination={"ToAddresses": [recipient]},
            Message={
                "Subject": {"Data": subject, "Charset": "UTF-8"},
                "Body": {"Text": {"Data": message, "Charset": "UTF-8"}}
            }
        )
    except ClientError as e:
        logger.error("SES send failed: %s", e.response["Error"]["Message"])
        return {
            "statusCode": 502,
            "body": json.dumps({"error": "Failed to send email"})
        }

    logger.info("Email sent to %s, messageId=%s", recipient, response["MessageId"])
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Email sent successfully",
            "messageId": response["MessageId"]
        })
    }
