\# Serverless Notification Application



A serverless notification application built using AWS services.



\## Architecture



Client

→ API Gateway

→ AWS Step Functions

→ AWS Lambda

→ Amazon SES

→ Email Notification



AWS SNS is also used for workflow completion notifications.



\## AWS Services Used



\- Amazon API Gateway

\- AWS Step Functions

\- AWS Lambda

\- Amazon SES

\- Amazon SNS

\- Amazon CloudWatch

\- AWS IAM



\## Features



\- Serverless architecture

\- REST API using API Gateway

\- Email notification using Amazon SES

\- Workflow orchestration using Step Functions

\- Retry and error handling

\- SNS workflow notification

\- CloudWatch monitoring

\- IAM-based security

\- CORS configuration



\## API Endpoint



POST /notify



Example request:



```json

{

&#x20; "email": "user@example.com",

&#x20; "subject": "Production Test",

&#x20; "message": "Testing the serverless notification application"

}

