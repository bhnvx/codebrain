import os
from typing import AsyncGenerator
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


load_dotenv(verbose=True)


engine = create_async_engine(
    f"postgresql+asyncpg://{os.get("user")}:{os.get("password")}@{os.get("host")}:{os.get("port")}/{os.get("database")}", echo=True, pool_pre_ping=True
)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        try:
            yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()