# pylint:disable = W0613
# unused-argument / W0613
import pytest
from .database_connection_handler import DbConnectionHandler

@pytest.mark.asyncio
async def test_database_connection_handler():
    async with DbConnectionHandler() as db_handler:
        assert db_handler.session is not None

@pytest.mark.asyncio
async def test_session_commit_on_exit(monkeypatch):
    committed = {"called": False}
    async def fake_commit():
        committed["called"] = True
    async def fake_close():
        pass

    async with DbConnectionHandler() as db_handler:
        db_handler.session.commit = fake_commit
        db_handler.session.close = fake_close
    assert committed["called"]

@pytest.mark.asyncio
async def test_session_rollback_on_exception(monkeypatch):
    rolled_back = {"called": False}
    async def fake_rollback():
        rolled_back["called"] = True
    async def fake_close():
        pass

    class TestException(Exception):
        pass

    try:
        async with DbConnectionHandler() as db_handler:
            db_handler.session.rollback = fake_rollback
            db_handler.session.close = fake_close
            raise TestException()
    except TestException:
        pass
    assert rolled_back["called"]
