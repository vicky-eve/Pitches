from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask
from app import app


bootstrap = Bootstrap()
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///pitches.db'
db = SQLAlchemy(app)

def create_app(config_name):
    app = Flask(__name__)
    

    #initialising the flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

from app import views
from app import models