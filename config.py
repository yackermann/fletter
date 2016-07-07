from flask_sqlalchemy import SQLAlchemy
import os, logging
from logging import Formatter

WTF_CSRF_ENABLED = True

# DB settings
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'fletter.db'
DEBUG = True
SECRET_KEY = 'secret_key'
USERNAME = 'admin'
PASSWORD = 'admin'

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = 'True'

# Configure logging
LOG_FILE = 'tmp/logfile.log'
LOG_LEVEL = logging.DEBUG

logging.basicConfig(filename = LOG_FILE,
                    level    = LOG_LEVEL)

logging.getLogger().addHandler(logging.StreamHandler())