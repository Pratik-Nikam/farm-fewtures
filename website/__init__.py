import os
from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
DB_NAME = "database.db"

# def create_app():
#     app = Flask(__name__)
#     # Set the base directory path
    
#     app.config.from_object(Config)

#     # Register the blueprint
#     app.register_blueprint(views)
    
#     # app = Flask(__name__, template_folder='templates')
#     # app.config['SECRET_KEY'] = 'fewcalc'
#     # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
#     # app.config['TESTING'] = False
#     # initialize this flask app with the sqlalchemy database 
#     db.init_app(app)
#     print(app.config, "==================")
#     from .views import views
#     app.register_blueprint(views, url_prefix = '/')

#     with app.app_context():
#         db.create_all()
  
#     return app


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import views here to avoid circular dependencies
    from .views import views

    # Register the blueprint
    app.register_blueprint(views)
    print(app.config, "==================")
    return app
 