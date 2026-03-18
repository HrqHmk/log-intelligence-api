from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from .db_engine import SessionLocal

class DbConnectionHandler():
    def __init__(self, session_factory=SessionLocal) -> None:
        self.session_factory = session_factory
        self.session:Optional[AsyncSession] = None

    async def __aenter__(self):
        self.session = self.session_factory()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.session.rollback()
        else:
            await self.session.commit()

        await self.session.close()
