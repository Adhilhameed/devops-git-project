# DevOps Git Project

A small Flask app, containerized with Docker and tested by GitHub Actions, used to practice **Git best practices**: branching, pull requests, tags, `.gitignore`, and documentation.

*DevOps Internship, Task 4 (Elevate Labs)*

## Project structure
```
app/            Flask app + tests
scripts/        deploy.sh
docs/           Git workflow notes (markdown)
.github/        CI workflow + PR template
Dockerfile, docker-compose.yml
```

## Run it
```bash
docker compose up --build
curl localhost:5000/health      # {"status":"ok"}
```
Without Docker:
```bash
pip install -r app/requirements.txt
cd app && pytest && python app.py
```

## Branching strategy
| Branch | Purpose |
|---|---|
| `main` | Stable, tagged releases only |
| `dev` | Integration branch |
| `feature/*` | New work, branched from `dev` |
| `hotfix/*` | Urgent fix, branched from `main` |

Flow: `feature/* -> PR -> dev -> PR -> main -> tag`

## Tags
`v1.0.0` stable release, `v1.0.1` hotfix.

## Docs
- [Git workflow](docs/git-workflow.md)
- [Merge conflict walkthrough](docs/conflict-resolution.md)
- [Advanced commands](docs/advanced-git.md)
- [Interview answers](docs/interview-answers.md)

## Screenshots
See `screenshots/` (branches, PRs, CI checks, tags).
