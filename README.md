# 📬 Serverless Notification Application

[![AWS](https://img.shields.io/badge/AWS-Serverless-orange?logo=amazonaws)](https://aws.amazon.com/serverless/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Deploy](https://github.com/Gnaneshambati1/serverless-notification-application/actions/workflows/deploy.yml/badge.svg)](https://github.com/Gnaneshambati1/serverless-notification-application/actions)

A production-style serverless notification system built on AWS — accepts a request via a REST API, orchestrates delivery through a Step Functions workflow with retry/error handling, sends email via Amazon SES, and publishes a completion event to SNS. Fully defined as Infrastructure-as-Code and deployed via an automated CI/CD pipeline.

---

## Architecture

Every component is provisioned via an [AWS SAM](https://aws.amazon.com/serverless/sam/) template — nothing is manually clicked together in the console.

---

## ✨ Features

- **Serverless, fully managed architecture** — no servers to patch or scale
- **REST API** via API Gateway with CORS support
- **Workflow orchestration** via Step Functions, including automatic retries and failure branching
- **Email delivery** via Amazon SES
- **Completion notifications** via Amazon SNS
- **Infrastructure as Code** — entire stack defined in `template.yaml` (AWS SAM)
- **CI/CD pipeline** — GitHub Actions runs lint + unit tests before every deploy, with OIDC-based AWS authentication (no long-lived credentials)
- **CloudWatch monitoring** for observability
- **Least-privilege IAM roles**

---

## 🛠️ Tech Stack

| Layer | Service |
|---|---|
| API | Amazon API Gateway |
| Orchestration | AWS Step Functions |
| Compute | AWS Lambda (Python 3.11) |
| Email | Amazon SES |
| Messaging | Amazon SNS |
| Monitoring | Amazon CloudWatch |
| IAM | AWS IAM (OIDC federated roles) |
| IaC | AWS SAM (CloudFormation) |
| CI/CD | GitHub Actions |
| Testing | pytest, flake8 |

---

## 📁 Project Structure

---

## 🚀 API Usage

**Endpoint:** `POST /notify`

**Request body:**
```json
{
  "email": "recipient@example.com",
  "subject": "Production Test",
  "message": "Testing the serverless notification application"
}
```

**Success response (200):**
```json
{
  "message": "Email sent successfully",
  "messageId": "0100019xxxx-xxxxxx"
}
```

**Error response (400 — missing email):**
```json
{
  "error": "Missing required field: 'email'"
}
```

---

## ⚙️ Deployment

### Prerequisites
- AWS account with SES sender identity verified
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed
- GitHub repository secrets configured: `AWS_ACCOUNT_ID`, `SES_SENDER_EMAIL`

### Deploy manually
```bash
sam build
sam deploy --guided \
  --stack-name serverless-notification-app \
  --parameter-overrides SenderEmail=your-verified-sender@example.com \
  --capabilities CAPABILITY_IAM
```

### Deploy via CI/CD
Every push to `main` automatically:
1. Runs `flake8` linting
2. Runs `pytest` unit tests
3. Deploys the stack via `sam deploy` — only if lint + tests pass

Authentication uses **GitHub OIDC federation** — no static AWS credentials are stored in the repo.

---

## 🧪 Running Tests Locally

```bash
pip install -r lambda/requirements-dev.txt
cd lambda
export SENDER_EMAIL=test@example.com
python -m pytest
```

---

## 🔒 Security Notes

- No credentials or account identifiers are hardcoded — all sensitive values are injected via GitHub Actions secrets and Lambda environment variables.
- Deployment uses short-lived, federated AWS credentials via OIDC rather than static IAM access keys.
- IAM roles follow least-privilege scoping.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Gnanesh Ambati**
[GitHub](https://github.com/Gnaneshambati1)
