from fastapi import FastAPI

from app.users.adapters.driver import user_router
from app.users.adapters.driver.rest_api.exception_handlers import add_exception_handlers


def create_web_app() -> FastAPI:
    web_app = FastAPI()

    web_app.include_router(user_router)

    return web_app


app = create_web_app()
add_exception_handlers(app)
