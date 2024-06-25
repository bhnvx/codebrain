import os
from typing import AsyncGenerator
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


load_dotenv(verbose=True)


engine = create_async_engine(
    f"postgresql+asyncpg://{os.environ.get('user')}:{os.environ.get('password')}@{os.environ.get('host')}:{os.environ.get('port')}/{os.environ.get('database')}",
    echo=True,
    pool_pre_ping=True,
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
