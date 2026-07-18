# 🚀 Local CI/CD Automation using GitHub Actions & Docker

A beginner-friendly DevOps project demonstrating how to build a Continuous Integration (CI) pipeline and design a Continuous Deployment (CD) workflow using GitHub Actions, Docker, and Docker Compose.

The project automates application building, dependency installation, Docker image creation, and prepares a deployment pipeline for remote servers.

---

## 📌 Features

- Dockerized Flask application
- Docker Compose configuration
- Git version control
- GitHub Actions CI pipeline
- Automatic dependency installation
- Automatic Docker image build
- Deployment automation script
- Ready for SSH-based deployment

---

## 🛠️ Tech Stack

- Python
- Flask
- Docker
- Docker Compose
- Git
- GitHub Actions
- Linux (Ubuntu / WSL)
- Bash

---

## 📂 Project Structure

```
CI-CD-Automation/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── deploy.sh
├── .gitignore
└── README.md
```

---

## ⚙️ CI Pipeline

Whenever code is pushed to the **main** branch:

1. GitHub Actions starts an Ubuntu runner.
2. Repository is cloned.
3. Python is installed.
4. Dependencies are installed.
5. Flask application is validated.
6. Docker image is built.

This ensures every commit can be successfully built inside a clean environment.

---

## 🚀 CD Pipeline Design

The deployment workflow is configured to:

1. Connect to a deployment server via SSH.
2. Pull the latest source code.
3. Stop existing containers.
4. Rebuild Docker images.
5. Restart the application using Docker Compose.

Deployment automation is implemented through:

```
deploy.sh
```

The workflow is ready to be executed against any reachable deployment server such as:

- AWS EC2
- Azure VM
- DigitalOcean
- Self-hosted GitHub Runner
- Local Linux server

---

## 🔄 CI Workflow

```
Developer
    │
git push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Checkout Repository
    ├── Install Python
    ├── Install Dependencies
    ├── Validate Flask App
    └── Build Docker Image
```

---

## 📦 CD Workflow (Designed)

```
GitHub Actions
        │
        ▼
SSH Connection
        │
        ▼
Deployment Server
        │
git pull
docker compose down
docker compose build
docker compose up -d
```

---

## 📖 Learning Outcomes

Through this project I learned:

- Docker fundamentals
- Docker Compose
- Git workflow
- GitHub Actions
- CI pipeline design
- Deployment automation
- Linux command line
- Bash scripting
- DevOps workflow fundamentals

---

## ⚠️ Current Limitation

The Continuous Deployment workflow has been fully implemented and tested locally.

Deployment from GitHub Actions to a remote server was not demonstrated because a publicly reachable deployment target (cloud VM or self-hosted runner) was intentionally not used.

The deployment workflow can be executed without modification on any reachable Linux server.

---

## 🔮 Future Improvements

- Self-hosted GitHub Runner
- Jenkins Pipeline
- Nginx Reverse Proxy
- Health Checks
- Automatic Rollback
- Monitoring with Prometheus & Grafana
- Kubernetes Deployment
- GitOps using ArgoCD

---

## License

MIT License
