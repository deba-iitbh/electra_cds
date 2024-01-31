from fastapi import FastAPI
from src.config.config import Config
from dotenv import load_dotenv, find_dotenv

from src.routes import api
from src.constants import Base, engine

# loading environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
app = FastAPI(root_path="/api")

# calling the dev configuration
config = Config().dev_config
Base.metadata.create_all(engine)
app.include_router(api, prefix="/v1")
