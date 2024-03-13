from typing import AsyncGenerator

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr



# from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from config import settings
ASYNC_DATABASE_URL = settings.DATABASE_URL_asyncpg
DATABASE_URL_psycopg = settings.DATABASE_URL_psycopg
# Base = declarative_base()
# metadata = MetaData()

engine = create_async_engine(ASYNC_DATABASE_URL, poolclass=NullPool, echo =True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


sync_engine = create_engine(
    url=DATABASE_URL_psycopg,
    # echo=True,
)
# для таски селери буду использовать синхронный коннект, иначе функцию придется делать асинхронной,
#  и с ней будут большие проблемы
sync_session_maker = sessionmaker(sync_engine)

class Base(DeclarativeBase):

    __abstract__ = True # при миграции эта таблица создаваться не будет

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session