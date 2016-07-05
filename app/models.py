from app import db
from time import time

class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)


    def __init__(self, text):
        self.text = text
        self.timestamp = int(time())

    def __repr__(self):
        return '<post {}>'.format(self.id)

    def json(self):
        return {
            'id' : self.id,
            'text' : self.text,
            'timestamp' : self.timestamp
        }