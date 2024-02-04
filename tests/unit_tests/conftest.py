"""pytest fixtures for Electra API"""

from unittest.mock import AsyncMock
import asyncio
import fakeredis.aioredis
from fastapi.testclient import TestClient
from fastapi import Request, HTTPException, status
import pytest
from mongomock_motor import AsyncMongoMockClient
from beanie import init_beanie
from httpx import AsyncClient

from src import app
form src.constants import get_current_user
from api.models import User, Subscription

BEARER_TOKEN = "Bearer \
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJib2IifQ.\
ci1smeJeuX779PptTkuaG1SEdkp5M1S1AgYvX8VdB20"

ADMIN_BEARER_TOKEN = "Bearer \
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.\
eyJzdWIiOiJib2IiLCJzY29wZXMiOlsiYWRtaW4iXX0.\
t3bAE-pHSzZaSHp7FMlImqgYvL6f_0xDUD-nQwxEm3k"

API_VERSION = "latest"
BASE_URL = f"http://testserver/{API_VERSION}/"


def mock_get_current_user(request: Request):
    """
    Get current active user
    """
    token = request.headers.get("authorization")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing token",
        )
    return User(
        id="65265305c74695807499037f",
        username="bob",
        hashed_password="$2b$12$CpJZx5ooxM11bCFXT76/z.o6HWs2sPJy4iP8."
        "xCZGmM8jWXUXJZ4L",
        email="bob@gmail.com",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )


def mock_get_current_admin_user(request: Request):
    """
    Get current active admin user
    """
    token = request.headers.get("authorization")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing token",
        )
    if token != ADMIN_BEARER_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden",
        )
    return User(
        id="653a5e1a7e9312c86f8f86e1",
        username="admin",
        hashed_password="$2b$12$CpJZx5ooxM11bCFXT76/z.o6HWs2sPJy4iP8."
        "xCZGmM8jWXUXJZ4K",
        email="admin@kernelci.org",
        groups=[],
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )

@pytest.fixture
def test_client():
    """Fixture to get FastAPI Test client instance"""
    # Mock dependency callables for getting current user
    with TestClient(app=versioned_app, base_url=BASE_URL) as client:
        return client


@pytest.fixture
async def test_async_client():
    """Fixture to get Test client for asynchronous tests"""
    async with AsyncClient(app=versioned_app, base_url=BASE_URL) as client:
        await versioned_app.router.startup()
        yield client
        await versioned_app.router.shutdown()


@pytest.fixture
def event_loop():
    """Create an instance of the default event loop for each test case.
    This is a workaround to prevent the default event loop to be closed by
    async pubsub tests. It was causing other tests unable to run.
    The issue has already been reported here:
    https://github.com/pytest-dev/pytest-asyncio/issues/371
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest.fixture
def mock_db_create(mocker):
    """Mocks async call to Database class method used to create object"""
    async_mock = AsyncMock()
    mocker.patch("api.db.Database.create", side_effect=async_mock)
    return async_mock
