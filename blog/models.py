from flask_sqlalchemy import  SQLAlchemy
from _datetime import datetime

db = SQLAlchemy()


category_entries = db.Table('category_entries',
                            db.Column('category_id', db.Integer(), db.ForeignKey('category.id')),
                            db.Column('entries_id', db.Integer(),  db.ForeignKey('entries.id')))



Entries_Tags = db.Table('entries_tags',
                        db.Column('entries_id', db.Integer(), db.ForeignKey('entries.id')),
                        db.Column('tag_id', db.Integer(), db.ForeignKey('tag.id')))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.Text(1000))
    is_visible = db.Column(db.Boolean(), default=True)
    entries = db.relationship('Entries', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Entries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    content = db.Column(db.Text, nullable=False)
    categorys = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    publish_status = db.Column(db.Boolean(), default=False)
    allow_reply = db.Column(db.Boolean(), default=False)
    stick = db.Column(db.Boolean(), default=False)
    create_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    update_date = db.Column(db.DateTime(), nullable=False, default=datetime.now, onupdate=datetime.now)
    comment = db.relationship('Comment',  backref='entries', lazy=True)
    tags = db.relationship('Tag', secondary=Entries_Tags, back_populates="entries")

    def __str__(self):
        return self.title


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(1000), nullable=False)
    entries_id = db.Column(db.Integer, db.ForeignKey('entries.id'), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    parent_content = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=True)

    def __str__(self):
        return self.content




class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    entries = db.relationship('Entries', secondary=Entries_Tags, back_populates="tags")
