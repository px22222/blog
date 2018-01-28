from flask import Flask
from flask_admin import Admin
from models import  db


def  create_app(config_file=None):
    app = Flask(__name__, instance_relative_config=True,
                instance_path='D:/Users/px222/PycharmProjects/flasker/config')

    app.config.from_pyfile('blog.conf')

    db.init_app(app)
    admin = Admin(app)
    return  app


def init_db():
    pass

app = create_app()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
