from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.db.main import initdb
from src.books.routes import book_router


# Lifespan event (Startup & Shutdown handler)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    print("Server is starting...")
    await initdb()
    
    yield  # Application runs here
    
    # Shutdown logic
    print("Server is stopping...")


# Create FastAPI app with metadata + lifespan
app = FastAPI(
    title="Bookly",
    description="A RESTful API for a book review web service",
    version="v1",
    lifespan=lifespan
)


# Include router
app.include_router(
    book_router,
    prefix="/api/v1/books",
    tags=["books"]
)
