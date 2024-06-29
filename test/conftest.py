import pytest
from fastapi import FastAPI

from main import app


@pytest.fixture
def application() -> FastAPI:
    return app
