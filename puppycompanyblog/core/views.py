# core/views.py

from flask import render_template,request,Blueprint

core = Blueprint('core',__name__)



@core.route('/')
def index():
    #more to come!
    return render_template('index.html')

