from flask import (current_app, Blueprint, render_template,
                   abort, redirect, url_for, request)
from flask_security import  current_user
from flask_admin.contrib.sqla import ModelView
from ..models import db, Entries, Category
from sqlalchemy import func


frontend_page = Blueprint('frontend', __name__, static_url_path='/')


def public_context():
    context = {}
    # 获取每个分类包含的博客数，对应原生sql语句:
    # select c.name, count(e.id) from category  c left join entries  e  on c.id = e.categorys group by c.name;
    category_entries_count = db.session.query(Category.id, Category.name, func.count(Entries.categorys)).join('entries').\
        group_by(Category.name).all()
    print (db.session.query(Entries.create_date.strftime("%Y-%m")).all())
    print (db.session.query(Entries.create_date).first()[0].strftime("%Y-%m"))
    context.update({'category_entries_count': category_entries_count})
    return context


@frontend_page.route('/')
def index():
    entries = Entries.query.all()
    context = public_context()
    context.update({'blogs': entries})
    return render_template('index.html', **context)


@frontend_page.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    blog = Entries.query.filter_by(id=blog_id).first()
    context = public_context()
    context.update({"blog_entries": blog})
    return render_template('blog_detail.html', **context)


@frontend_page.route('/category/<int:category_id>')
def category_page(category_id):
    entries = Category.query.filter_by(id=category_id).first().entries
    context = public_context()
    context.update({"category_entries": entries})
    return render_template('category_page.html', **context )






