from . import db
from datetime import datetime



class User(db.Model):                      #connecting our class to the database to allow communication
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    downvote = db.relationship('Downvote',backref = 'user',lazy="dynamic")
    upvote= db.relationship('Upvote',backref = 'user',lazy="dynamic")
    comment= db.relationship('Comment',backref = 'user',lazy="dynamic")
    pitch= db.relationship('Pitch',backref = 'user',lazy="dynamic")



    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
     __tablename__ = 'pitches'
     id = db.Column(db.Integer,primary_key = True)
     title = db.Column(db.String(255))
     word = db.Column(db.Text())
     time = db.Column(db.DateTime, default = datetime.utcnow)
     category = db.Column(db.String(255), index = True)
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
     downvote = db.relationship('Downvote',backref = 'pitch',lazy="dynamic")
     upvote= db.relationship('Upvote',backref = 'pitch',lazy="dynamic")
     comment= db.relationship('Comment',backref = 'pitch',lazy="dynamic")

     def __repr__(self):
        return f'Pitch {self.word}'






class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'





class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'





class Comment(db.Model):
     __tablename__ = 'comments'
     id = db.Column(db.Integer,primary_key = True)
     comment = db.Column(db.String (255), index=True)
     pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

     def __repr__(self):
        return f'comment:{self.comment}'
