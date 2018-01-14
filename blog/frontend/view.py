from flask import current_app, Blueprint, render_template

frontend_page = Blueprint('frontend', __name__)


@frontend_page.route('/')
def hello_world():
    return 'hello, world!'

