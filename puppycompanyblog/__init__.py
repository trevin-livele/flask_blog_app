#puppy company blog /__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

######################################
####### DATABASE SETUP ###############
######################################
# 'postgresql+psycopg2://moringa:ashihundu@localhost/pitch'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:ashihundu@localhost/blog'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#######################################

#login configs
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'






from puppycompanyblog.core.views import core
from puppycompanyblog.users.views import users
from puppycompanyblog.blog_posts.views import blog_posts
from puppycompanyblog.error_pages.handlers import error_pages



app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)