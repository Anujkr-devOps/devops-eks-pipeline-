# Assignment 3 – DevOps CI/CD Pipeline with AKS

## Overview
This project demonstrates a **CI/CD pipeline** for a Flask web application using:
- **GitHub Actions** for automation
- **Docker** for containerization
- **Azure Container Registry (ACR)** for image storage
- **Azure Kubernetes Service (AKS)** for deployment

---

## Features Implemented So Far
- **Source Code Management**: GitHub repository with workflow configuration.
- **Automated Testing**:
  - Added `pytest` for unit testing.
  - Pipeline runs tests before building Docker image.
- **Containerization**:
  - Dockerfile based on `python:3.11-slim`.
  - Exposes port `5000` for Flask.
- **Deployment**:
  - CI/CD pipeline builds and pushes Docker image to ACR.
  - Deploys to AKS using Kubernetes manifests (`deployment.yaml`, `service.yaml`).

---

## Project Structure
app/
app.py
requirements.txt
tests/
test_app.py
K8s/
deployment.yaml
service.yaml
.github/workflows/
aks-cicd.yml
Dockerfile

## CI/CD Workflow Steps
1. **Checkout Code**
2. **Install Dependencies & Run Tests**
   - Creates virtual environment
   - Installs packages from `requirements.txt`
   - Runs `pytest` on `tests/`
3. **Azure Login**
4. **Login to ACR**
5. **Build & Push Docker Image**
   - Tags image with `github.sha`
6. **Set AKS Context**
7. **Deploy to AKS**
   - Applies Kubernetes manifests
   - Updates deployment image

---

## How to Run Locally
```bash
# Clone repo
git clone <https://github.com/Anujkr-devOps/devops-eks-pipeline-.git>
cd <devops-eks-pipeline-.git>

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r app/requirements.txt

# Run tests
pytest tests/

# Run Flask app
python app/app.py