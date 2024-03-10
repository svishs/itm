from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr



# from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from config import settings
DATABASE_URL = settings.DATABASE_URL_asyncpg

# Base = declarative_base()
# metadata = MetaData()

engine = create_async_engine(DATABASE_URL, poolclass=NullPool)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):

    __abstract__ = True # при миграции эта таблица создаваться не будет

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session