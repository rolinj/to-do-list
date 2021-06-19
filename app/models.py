from hashlib import md5
from app import db, models


class Task(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(120))
    date     = db.Column(db.String(15))


    def __repr__(self):
        return '<Activity %r>' % (self.activity)