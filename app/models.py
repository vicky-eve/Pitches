from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):                      #connecting our class to the database to allow communication
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    downvote = db.relationship('Downvote',backref = 'user',lazy="dynamic")
    upvote= db.relationship('Upvote',backref = 'user',lazy="dynamic")
    comment= db.relationship('Comment',backref = 'user',lazy="dynamic")
    pitch= db.relationship('Pitch',backref = 'user',lazy="dynamic")

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
     __tablename__ = 'pitches'
     id = db.Column(db.Integer,primary_key = True)
     title = db.Column(db.String(255))
     word = db.Column(db.Text())
     timelapse = db.Column(db.DateTime, default = datetime.utcnow)
     category = db.Column(db.String(255), index = True)
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
     downvote = db.relationship('Downvote',backref = 'pitch',lazy="dynamic")
     upvote= db.relationship('Upvote',backref = 'pitch',lazy="dynamic")
     comment= db.relationship('Comment',backref = 'pitch',lazy="dynamic")

     def save_pitch(self):
        db.session.add(self)
        db.session.commit()

     def __repr__(self):
        return f'Pitch {self.word}'






class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'





class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

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
