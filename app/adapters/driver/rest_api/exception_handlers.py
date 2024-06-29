from fastapi import FastAPI

from app.users.domain.exceptions import UserNotFound
from .handlers import resource_not_found_handler


def add_exception_handlers(app: FastAPI) -> None:
    app.exception_handler(UserNotFound)(resource_not_found_handler)
