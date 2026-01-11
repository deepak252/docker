from fastapi import FastAPI
from app.routes import country, media_channel, company, product, product_media
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

app.include_router(country.router, prefix="/api/v1")
app.include_router(media_channel.router, prefix="/api/v1")
app.include_router(company.router, prefix="/api/v1")
app.include_router(product.router, prefix="/api/v1")
app.include_router(product_media.router, prefix="/api/v1")

# Custom business error handler
app.add_exception_handler(AppException, app_exception_handler)
# Catch-all fallback for ANY other exception
app.add_exception_handler(Exception, unhandled_exception_handler)
