"""pytest fixtures for Electra API"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
import asyncio
from fastapi import Request, HTTPException, status
import pytest
from unittest.mock import Mock
from sqlalchemy.orm import Session

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# this is to include backend dir in sys.path so that we can import from db,main.py

from src import app

# from src.constants import get_current_user


API_VERSION = "v1"
BASE_URL = f"http://localhost:5000/api/{API_VERSION}/"


@pytest.fixture
def mock_db():
    return Mock(spec=Session)


@pytest.fixture
def testclient():
    with TestClient(app=app, base_url=BASE_URL) as client:
        return client


@pytest.fixture
def mock_get_current_user(request: Request):
    token = request.headers.get("authorization")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing token",
        )
    return User()


app.dependency_overrides[get_current_user] = mock_get_current_user

# app.dependency_overrides[get_current_superuser] = mock_get_current_admin_user
