import traceback
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError


class AppException(HTTPException):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail=message)


async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "code": exc.status_code,
            "message": exc.detail,
        }
    )


async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    # log exact DB error
    print("SQLAlchemy Error:", exc)

    return JSONResponse(
        status_code=500,
        content={
            "code": 500,
            "message": "Database error occurred",
        }
    )


async def unhandled_exception_handler(request: Request, exc: Exception):
    # Print or log the full traceback to your log system
    print("UNEXPECTED ERROR:", repr(exc))
    traceback.print_exc()

    return JSONResponse(
        status_code=500,
        content={
            "code": 500,
            "message": "Internal server error",
        }
    )