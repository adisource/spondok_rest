from flask import Flask
from importlib import import_module
from config import Config
from pyrebase import pyrebase

def register_blueprints(app):


    for module_name in ('wali','admin_pondok'):
        module = import_module('App.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)



def create_app(selemium=False):
    app = Flask(__name__)

    register_blueprints(app)
    
    
    return app

db = Config.firebase.database()
auth = Config.firebase.auth()




    