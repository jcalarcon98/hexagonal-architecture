from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.users.domain.exceptions import UserNotFound


def resource_not_found_handler(_: Request, exception: Exception):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error_message": str(exception)
        }
    )


def add_exception_handlers(app: FastAPI) -> None:
    app.exception_handler(UserNotFound)(resource_not_found_handler)
