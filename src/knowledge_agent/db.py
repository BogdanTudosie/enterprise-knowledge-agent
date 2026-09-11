from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

from knowledge_agent.config import get_settings


def create_db_engine() -> Engine:
    return create_engine(get_settings().database_url, pool_pre_ping=True)


def database_is_healthy(engine: Engine) -> bool:
    with engine.connect() as connection:
        return connection.execute(text("SELECT 1")).scalar_one() == 1
