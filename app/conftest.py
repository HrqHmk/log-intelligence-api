# pylint:disable = W1514
import os
from pathlib import Path
import pytest
import pytest_asyncio
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

load_dotenv()

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

@pytest_asyncio.fixture(autouse=True)
async def setup_and_teardown_db(session_factory):
    sql_path = Path("init/seed_log.sql")

    async with session_factory() as session:
        await session.execute(text("TRUNCATE TABLE request_logs RESTART IDENTITY CASCADE"))

        with open(sql_path, "r") as f:
            sql_script = f.read()

        await session.execute(text(sql_script))
        await session.commit()

    yield
    async with session_factory() as session:
        await session.execute(text("TRUNCATE TABLE request_logs RESTART IDENTITY CASCADE"))
        await session.commit()

@pytest.fixture(name="engine")
def engine_fixture():
    return create_async_engine(TEST_DATABASE_URL)

@pytest.fixture(name="session_factory")
def session_factory_fixture(engine):
    return sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

@pytest_asyncio.fixture
async def db_session(session_factory):
    async with session_factory() as session:
        trans = await session.begin()
        try:
            yield session
        finally:
            await trans.rollback()
