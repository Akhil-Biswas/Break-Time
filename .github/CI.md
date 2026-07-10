# CI Documentation

## Location
Workflow file: `.github/workflows/ci.yml`
Triggered on: push and pull requests to `main` and `dev` branches

## Environment
All jobs run inside Docker containers built from the project's `Dockerfile`,
ensuring consistent environments between local development and CI.

## Jobs

| Job              | Purpose                          | Tool        |
|-------------------|-----------------------------------|-------------|
| type-check        | Validates type hints              | mypy        |
| lint               | Checks code style                 | flake8      |
| format-check       | Verifies formatting (no changes)  | black       |
| unit-tests         | Runs isolated unit tests + coverage | pytest / pytest-cov |
| integration-tests  | Tests app with real DB/services   | docker compose + pytest |
| security           | Scans code for vulnerabilities    | bandit      |
| dependency-check   | Scans dependencies for CVEs       | pip-audit   |

## Execution
- All jobs run in **parallel** (no `needs:` dependency set).
- Each job builds a Docker image and runs commands inside it via `docker run`
  (or `docker compose` for jobs needing multiple services).

## Adding a new test type
1. Add a new job under `jobs:` in `ci.yml`.
2. Reuse the existing Dockerfile, or create a new one if dependencies differ.
3. Add `needs: [job-name]` if it must run after another job.

## Local testing (before pushing)
Run the same commands used in CI locally to reproduce results:
```bash
docker build -t myapp:test .
docker run --rm myapp:test pytest
