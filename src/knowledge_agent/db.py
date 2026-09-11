from sqlalchemy import create_engine, select
from sqlalchemy.engine import Engine

from knowledge_agent.config import get_settings


def create_db_engine() -> Engine:
    return create_engine(get_settings().database_url, pool_pre_ping=True)


def database_is_healthy(engine: Engine) -> bool:
    with engine.connect() as connection:
        value = connection.execute(select(1)).scalar_one()
        return bool(value)
