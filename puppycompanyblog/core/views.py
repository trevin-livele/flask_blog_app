# core/views.py
from puppycompanyblog.models import BlogPost,Comment
from flask import render_template,request,Blueprint
from puppycompanyblog import db

core = Blueprint('core',__name__)



@core.route('/')
def index():
    db.create_all()
    page = request.args.get('page',1,type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page = page,per_page=5)
    comments = Comment.query.all()
    return render_template('index.html',blog_posts=blog_posts,comments=comments)

@core.route('/info')
def info():
    return render_template('info.html')


    