from .wsgi import create_app
from .models import db


app = create_app()


@app.cli.command()
def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
