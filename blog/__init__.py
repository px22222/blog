from flask_security import  SQLAlchemyUserDatastore
from .wsgi import create_app
from .models import db
from .myadmin.models import User, Role



app = create_app()


@app.cli.command()
def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        user_datastore.create_user(username='pengxuan', email='176126991@qq.com', password='password')
        db.session.commit()
