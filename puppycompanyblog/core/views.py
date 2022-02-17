# core/views.py
from puppycompanyblog.models import BlogPost,Comment
from flask import render_template,request,Blueprint,url_for,redirect
from puppycompanyblog import db,mail
from puppycompanyblog.blog_posts.forms import SuscribeForm
from flask_mail import Message




core = Blueprint('core',__name__)




def subscribe(email):
    msg=Message('@noReply',sender='trevin.livele@student.moringaschool.com',recipients=[email])
    msg.body=f'''You have successfully subscribed to our news letter.
If you didn't subscibe ,kindly ignore message.
                '''
    mail.send(msg)    





@core.route('/',methods=['POST', 'GET'])
def index():
    db.create_all()
    page = request.args.get('page',1,type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page = page,per_page=5)
    comments = Comment.query.all()
    form = SuscribeForm()
    if form.validate_on_submit():
        email=form.content.data
        subscribe(email)
        return redirect(url_for('core.index'))
    return render_template('index.html',blog_posts=blog_posts,comments=comments,form=form)






@core.route('/info')
def info():
    return render_template('info.html')


    