from fastapi import FastAPI, HTTPException

from knowledge_agent.db import create_db_engine, database_is_healthy

app = FastAPI(title="Enterprise Knowledge Agent")
engine = create_db_engine()


@app.get("/health")
def health() -> dict[str, str]:
    try:
        if not database_is_healthy(engine):
            raise HTTPException(status_code=503, detail="Database unhealthy")
    except Exception as exc:
        if isinstance(exc, HTTPException):
            raise
        raise HTTPException(status_code=503, detail="Database unavailable") from exc

    return {"status": "ok", "database": "ok"}
