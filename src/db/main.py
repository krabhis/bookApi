from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.config import Config
from sqlmodel import SQLModel
from src.books.models import Book

# async engine using SQLAlchemy async utilities
engine = create_async_engine(
    Config.DATABASE_URL,
    echo=True,
    connect_args={"ssl": True},
)


async def initdb():
    """create our database models in the database"""

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = async_sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session