from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy import String, Boolean


db = SQLAlchemy()


category_entries = db.table('category_entries',
                            db.Column('category_id', db.Integer(), db.ForeignKey('category.id')),
                            db.Column('entries_id', db.Integer(),  db.ForeignKey('entries.id')))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.Text(1000))
    is_visible = db.column(db.Boolean)


class Entries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text, nullable=False)
    categorys = db.relationship('Category', secondary=category_entries,
                                backref=db.backref('entries', lazy='dynamic'))



