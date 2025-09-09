from fastapi import FastAPI
from app.database.connection import Base, engine
from app.api import auth_routes, todo_routes

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Todo App")

app.include_router(auth_routes.router)
app.include_router(todo_routes.router)
