# coding=utf-8;

import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    image = db.Column(db.String(100), nullable=True)
    added_on = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now())

    def __init__(self, username, first_name, last_name, age, gender=0):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.user_id = User.generate_user_id()

    @staticmethod
    def generate_user_id():
        from time import time

        new_id = time()
        new_id = str(long(new_id))
        return long(new_id)

    def get_gender_display(self):
        from forms import GENDER
        return GENDER[self.gender]

    def __repr__(self):
        return u'<User {0}>'.format(self.username)

    def get_image_url(self):
        return '/uploads/{0}'.format(self.image)

    def to_json(self):
        return json.dumps({
            "userid": self.user_id,
            "username": self.username,
            "image": "...",
            "gender": self.get_gender_display(),
            "age": self.age,
            "profile_add_on": self.added_on.strftime("%Y-%m-%d"),
            })