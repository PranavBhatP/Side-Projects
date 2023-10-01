from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db=SQLAlchemy() # Creating a database from an SQLAlchemy object
DB_NAME = "database.db"

def create_app():
    app  = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key123$%'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, rl_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User, Note

    with app.app_context():
        db.create_all()

    return app

