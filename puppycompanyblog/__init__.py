#puppy company blog /__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

app = Flask(__name__)



######################################
####### DATABASE SETUP ###############
######################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#######################################








from puppycompanyblog.core.views import core
from puppycompanyblog.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(error_pages)