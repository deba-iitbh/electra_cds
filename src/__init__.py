from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv, find_dotenv

from src.config.config import Config
from src.routes import api
from src.constants import Base, engine

# loading environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

app = FastAPI(root_path="/api")
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# calling the dev configuration
config = Config().dev_config
Base.metadata.create_all(engine)
app.include_router(api, prefix="/v1")