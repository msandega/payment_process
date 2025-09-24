[![Django CI/CD Pipeline](https://github.com/msandega/payment_process/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/msandega/payment_process/actions/workflows/ci-cd.yml)

This project implements a complete CI/CD pipeline for a Django REST API Payment Gateway with Docker containerization, automated testing, and cloud deployment.

This project demonstrates **real-world DevOps practices** by taking a Django REST Framework (DRF) based **Payment Gateway API**, containerizing it with Docker, automating testing & deployment with GitHub Actions, and deploying it on the cloud (Render/Railway).  

The backend team developed the API — this task focuses on **DevOps automation, reliability, and deployment**.

---

## 🚀 Tech Stack
- **Backend:** Django REST Framework (DRF)
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Security:** Bandit, Trivy
- **Cloud Deployment:** Render / Railway
- **Registry:** Docker Hub / GitHub Container Registry (GHCR)

---

## 🛠 Features
- RESTful API for handling payment initialization & status checks
- Fully containerized with **Docker**
- Automated pipeline for **tests, linting, and security scans**
- Auto-deploys to cloud on merge to `main`
- Secrets securely managed in **GitHub Actions**
- Live demo URL exposed for testing

---

## 📦 Containerization

### Build Image
```bash
docker build -t payments-api .

Run Container
docker run -p 8000:8000 --env-file .env payments-api

🔄 CI/CD Pipeline
On Pull Request

✅ Run unit tests (python manage.py test)

🔍 Linting & security scans (bandit, trivy)

On Merge to main

🏗️ Build & push Docker image to Docker Hub/GHCR

🚀 Auto-deploy containerized app to Render/Railway

🖥️ Deployment

🔗 Live API URL:
👉 https://payments-api.onrender.com/api/v1/payments

🔐 Secrets Management

All sensitive credentials (e.g., Paystack / Flutterwave / PayPal sandbox keys) are stored in GitHub Secrets:

SECRET_KEY

DATABASE_URL

PAYSTACK_SECRET_KEY

FLUTTERWAVE_SECRET_KEY

📑 Example API Usage
Initialize Payment
curl -X POST https://payments-api.onrender.com/api/v1/payments/ \
     -H "Content-Type: application/json" \
     -d '{"amount": 1000, "currency": "USD", "email": "user@example.com"}'

Check Payment Status
curl https://payments-api.onrender.com/api/v1/payments/<payment_id>/

📂 Project Structure
.
├── .github/workflows/django.yml   # CI/CD pipeline
├── Dockerfile                     # Docker image definition
├── .dockerignore                  # Files excluded from Docker builds
├── payment_process/               # Django project
├── payments/                      # Payments app (API logic)
└── README.md                      # Documentation
