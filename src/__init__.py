from flask import Flask
import os
from src.config.config import Config
from datetime import timedelta
from dotenv import load_dotenv, find_dotenv
from src.routes import api
from src.constants import db, bcrypt, jwt

# loading environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
app = Flask(__name__)

# calling the dev configuration
config = Config().dev_config

# making our application to use dev env
# app.env = config.ENV

# load the secret key defined in the .env file
app.secret_key = os.environ.get("SECRET_KEY")

# Options
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
# Disable Flask-SQLAlchemy modification tracker
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_COOKIE_SECURE"] = os.environ.get("JWT_COOKIE_SECURE")
app.config["JWT_COOKIE_CSRF_PROTECT"] = False  # change in prod
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

# bcrypt
bcrypt.init_app(app)
# jwt
jwt.init_app(app)


# sql alchemy instance
db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(api, url_prefix="/api/v1")
