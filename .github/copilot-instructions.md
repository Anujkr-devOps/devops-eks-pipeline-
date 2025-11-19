<!-- .github/copilot-instructions.md
Purpose: concise, repo-specific guidance for AI coding assistants
Generated: by repo assistant on user's request
-->
# Copilot / AI Agent Instructions

Summary
- This repository contains a tiny Flask web application (in `app/`) packaged with a `Dockerfile` for container-based deployment. The project README references a CI/CD pipeline using GitHub Actions, ECR and EKS.

Big picture
- Web app: `app/app.py` — single-file Flask app exposing `/` on port 5000.
- Packaging: top-level `Dockerfile` builds the container using `python:3.11-slim`, installs `app/requirements.txt`, then copies `app/` into the image and runs `app.py`.
- CI/CD intent: README states GitHub Actions + ECR + EKS; there are no workflow files in this repo root to rely on, so assume pipeline definitions are external or will be added under `.github/workflows/`.

Key files to read
- `app/app.py` — application entrypoint and primary logic.
- `app/requirements.txt` — pinned Python deps; use for local/dev installs and in Docker builds.
- `Dockerfile` — build steps and runtime command; note how files are copied (`COPY app/requirements.txt .` then `COPY  app/ .`).
- `README.md` — project intent and high-level CI/CD goals.

Developer workflows (concrete commands)
- Build the Docker image (from repo root):
```powershell
docker build -t flask-eks-app .
```
- Run container locally (map port 5000):
```powershell
docker run -p 5000:5000 flask-eks-app
```
- Run the app locally without Docker (from repo root):
```powershell
python -m pip install -r app/requirements.txt; cd app; python app.py
```

Project-specific patterns & gotchas
- File layout matters for the `Dockerfile`: it expects `app/requirements.txt` in the `app` directory and copies everything from `app/` into the container root. If you change locations, update the `Dockerfile` accordingly.
- The Flask app is minimal and runs on `0.0.0.0:5000` (good for container exposure). Avoid changing the host binding unless producing a development-only branch.
- Dependencies are pinned in `app/requirements.txt`; prefer pinning when adding libs and update the Docker build step to use the updated file.

What an AI assistant should do first
- Inspect `app/app.py` and `Dockerfile` to understand runtime behavior and build context.
- Verify whether `.github/workflows/` exists; if not, note that CI config is absent and ask the maintainers for desired pipeline YAMLs (ECR/EKS configs).
- If tasked to add tests or linting, propose minimal tooling (e.g. `pytest`, `flake8`) and show how to add those to `requirements-dev.txt` and CI workflows.

Examples to reference in PRs or changes
- When modifying runtime code, include a short local test: a `curl http://localhost:5000/` after `docker run` or running `python app/app.py`.
- When changing Docker behavior, update the `Dockerfile` and include the exact `docker build` and `docker run` commands that were used to validate the change.

Notes & assumptions
- Current branch: `app_deploy` (local workspace). Repo name: `devops-eks-pipeline-`.
- Host environment used by the developer is Windows PowerShell; provided commands use PowerShell syntax where appropriate.
- There are no repository-level CI workflow files discovered during the initial pass; if there are secrets/credentials needed for ECR/EKS, those will not be present here and require collaborator configuration in GitHub Actions.

If anything below is unclear or you want additional coverage (e.g., suggested GitHub Actions workflow templates, tests, or a health-check endpoint), tell me which area to expand and I'll update this file.
