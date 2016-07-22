from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

app.url_map.strict_slashes = False

from app import post_routes, static_routes
from app import models