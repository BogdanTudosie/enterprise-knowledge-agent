# Enterprise Knowledge Agent

A hands-on portfolio project for developing practical Data & GenAI Engineering skills.

The project will grow from a tested Python/PostgreSQL service into an enterprise-oriented data and GenAI platform with ETL/ELT pipelines, lakehouse concepts, document ingestion, RAG, MCP tools, agentic workflows, and Azure deployment.

## Milestone 0 — Engineering Foundation

Initial stack:

- Python 3.12+
- FastAPI
- SQLAlchemy 2
- PostgreSQL
- Pydantic Settings
- pytest
- Ruff
- mypy
- Docker Compose
- GitHub Actions

The first application endpoint is `GET /health`. Unlike a superficial health endpoint, it executes `SELECT 1` against PostgreSQL so the integration test verifies the application/database boundary.

## Architecture

```text
Client
  |
  v
FastAPI
  |
  v
SQLAlchemy
  |
  v
PostgreSQL
```

This architecture will evolve throughout the learning program.

## Local development

Prerequisites: Python 3.12+, Docker, and `uv`.

```bash
cp .env.example .env
docker compose up -d db
uv sync --dev
uv run pytest
uv run uvicorn knowledge_agent.main:app --reload
```

Then open `http://127.0.0.1:8000/health`.

## Learning approach

Every major capability added to this repository should be implemented, tested, documented, and connected to a concrete Data & GenAI Engineering skill. The aim is not to accumulate tutorial code; it is to produce one coherent system that can be discussed credibly in technical interviews.
