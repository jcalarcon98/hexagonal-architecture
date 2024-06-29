from fastapi import FastAPI

from app.users.adapters.driver import user_router
from .exception_handlers import add_exception_handlers


def create_web_app() -> FastAPI:
    web_app = FastAPI()

    web_app.include_router(user_router)

    add_exception_handlers(web_app)
    return web_app

