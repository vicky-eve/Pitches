from . import db

class User(db.Model):                      #connecting our class to the database to allow communication
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))