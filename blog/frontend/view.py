from flask import (current_app, Blueprint, render_template,
                   abort, redirect, url_for, request)
from flask_security import  current_user
from flask_admin.contrib.sqla import ModelView
from ..models import  db, Entries



frontend_page = Blueprint('frontend', __name__, static_url_path='/')


@frontend_page.route('/')
def index():
    entries = Entries.query.all()
    return  render_template('index.html', blogs=entries)



@frontend_page.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    blog = Entries.query.filter_by(id=blog_id).first()
    return render_template('blog_detail.html', entries=blog)





