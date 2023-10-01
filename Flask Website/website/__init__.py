from flask import Flask

def create_app():
    app  = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key123$%'


    from .views import views
    from .auth import auth

    app.register_blueprint(views, rl_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/') 
    return app

