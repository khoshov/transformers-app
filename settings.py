import os.path
from pathlib import Path

from environs import Env

env = Env()
env.read_env('.env')

ENV = env.str("FLASK_ENV", default="development")
DEBUG = ENV == "development"
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SECRET_KEY = env.str("SECRET_KEY")
SQLALCHEMY_TRACK_MODIFICATIONS = False
BASE_DIR = Path(__file__).resolve()
MEDIA_DIR = os.path.join(os.path.dirname(BASE_DIR), 'media')
