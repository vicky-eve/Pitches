from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask
from config import config_options
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE
import os 






login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)

mail = Mail()
simple = SimpleMDE()



def create_app(config_name):
    app = Flask(__name__)
    app.config['UPLOADED_PHOTOS_DEST'] = 'static/photos' 
    app.config.from_object(config_options[config_name])
    configure_uploads(app,photos)    #configure upload set
     
    #initialising the flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

     # configure UploadSet
    configure_uploads(app,photos)

    app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://vicky:aderazi@localhost/pitches'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    return app

