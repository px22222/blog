import pymysql
from flask import Flask
from flask_admin import Admin
from .models import  db
from .frontend.view import frontend_page
from .myadmin.view import admin_page


def create_app(config_file=None):
    pymysql.install_as_MySQLdb()
    app = Flask(__name__, instance_relative_config=True,
                instance_path='D:\\Users\\px222\\PycharmProjects\\flasker\\blog\\config')

    app.config.from_pyfile('blog.conf')

    db.init_app(app)
    admin = Admin(app)
    app.register_blueprint(admin_page)
    app.register_blueprint(frontend_page)
    return  app

