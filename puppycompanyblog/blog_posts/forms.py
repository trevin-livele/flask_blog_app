# blog_posts/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,EmailField
from wtforms.validators import DataRequired


class BlogPostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    text = TextAreaField('Text',validators=[DataRequired()])
    submit = SubmitField("Post")

class SuscribeForm(FlaskForm):
    content = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Subscribe')






    