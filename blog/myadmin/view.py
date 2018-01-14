from flask import current_app, Blueprint, render_template

admin_page = Blueprint('admin_page', __name__)


@admin_page.route('/adminpage')
def hello_admin():
    return 'hello, admin'

