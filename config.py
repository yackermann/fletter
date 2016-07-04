from flask_sqlalchemy import SQLAlchemy
import os

WTF_CSRF_ENABLED = True

# DB settings
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'fletter.db'
DEBUG = True
SECRET_KEY = 'you-will-never-guess'
USERNAME = 'admin'
PASSWORD = 'admin'

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = 'True'