import pymysql
from flask import Flask, url_for
from flask_admin import Admin, helpers as admin_helpers
from flask_security import SQLAlchemyUserDatastore, Security
from .models import  db, Category, Entries, Comment, category_entries
from .frontend.view import frontend_page
from .myadmin.view import admin_page, entries_modelview
from .myadmin.models import  Role, User



def create_app(config_file=None):
    pymysql.install_as_MySQLdb()
    app = Flask(__name__, instance_relative_config=True,
                instance_path='/tmp/test/blog/blog/config')

    app.config.from_pyfile('blog.conf')

    db.init_app(app)
    admin = Admin(app)
    admin.add_view(entries_modelview(Entries, db.session))
    app.register_blueprint(admin_page)
    app.register_blueprint(frontend_page)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    @security.context_processor
    def security_context_processor():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=admin_helpers,
            get_url=url_for
        )
    return  app

