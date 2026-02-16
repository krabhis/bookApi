# # Inside main.py title
# from fastapi import FastAPI
# from src.books.routes import book_router

# version = 'v1'

# app = FastAPI(
#     title='Bookly',
#     description='A RESTful API for a book review web service',
#     version=version,
# )

# app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])  


from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager


#the lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):    
    print("Server is starting...")
    yield
    print("server is stopping")



app = FastAPI(
    lifespan=lifespan # add the lifespan event to our application
)

app.include_router(
    book_router,
    prefix="/books",
    tags=['books']
)