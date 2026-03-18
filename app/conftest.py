import os
import pytest
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

@pytest.fixture(scope="session", name="engine")
def engine_fixture():
    return create_async_engine(TEST_DATABASE_URL)

@pytest.fixture(scope="session", name="session_factory")
def session_factory_fixture(engine):
    return sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

@pytest.fixture
async def db_session(session_factory):
    async with session_factory() as session:
        trans = await session.begin()
        try:
            yield session
        finally:
            await trans.rollback()
