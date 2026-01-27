import time
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request

from app.core.logging import setup_logging
from app.core.elasticsearch import connect_elasticsearch, close_elasticsearch
from app.indices.product_index import create_product_index
from app.routes.router import api_router

setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---- Startup ----
    logger.info("Application startup initiated")

    await connect_elasticsearch()
    await create_product_index()

    logger.info("Application startup completed")
    yield

    # ---- Shutdown ----
    logger.info("Application shutdown initiated")
    await close_elasticsearch()
    logger.info("Application shutdown completed")


app = FastAPI(
    title="FastAPI Elasticsearch Service",
    lifespan=lifespan
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    logger.info(
        f"{request.method} {request.url.path} "
        f"status={response.status_code} "
        f"time={duration:.3f}s"
    )
    return response


app.include_router(api_router)
