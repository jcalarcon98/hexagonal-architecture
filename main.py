from fastapi import FastAPI

from app.users.controller import user_router


def create_web_app() -> FastAPI:
    web_app = FastAPI()

    web_app.include_router(user_router)

    return web_app


app = create_web_app()
