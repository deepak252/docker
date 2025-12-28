from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import users
from app.core.exceptions import (
    AppException, 
    app_exception_handler, 
    sqlalchemy_exception_handler, 
    unhandled_exception_handler
)
from sqlalchemy.exc import SQLAlchemyError

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Production fastapi project")

@app.get('/')
def home():
    return {
        "status": "ok",
        "message": "fastapi application"
    }

# app.include_router(users.router, prefix="/api")
app.include_router(users.router, prefix="")

# Custom business error handler
app.add_exception_handler(AppException, app_exception_handler)
# SQLAlchemy DB exceptions
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)
# Catch-all fallback for ANY other exception
app.add_exception_handler(Exception, unhandled_exception_handler)
