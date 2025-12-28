from fastapi import FastAPI
from app.routes import producer
from app.core.exceptions import (
    AppException, 
    app_exception_handler, 
    unhandled_exception_handler
)

app = FastAPI(title="producer fastapi")

@app.get('/')
def home():
    return {
        "status": "ok",
        "message": "producer is up"
    }

# app.include_router(users.router, prefix="/api")
app.include_router(producer.router, prefix="")

# Custom business error handler
app.add_exception_handler(AppException, app_exception_handler)
# Catch-all fallback for ANY other exception
app.add_exception_handler(Exception, unhandled_exception_handler)
