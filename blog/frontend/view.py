from flask import (current_app, Blueprint, render_template,
                   abort, redirect, url_for, request)
from flask_security import  current_user
from flask_admin.contrib.sqla import ModelView



frontend_page = Blueprint('frontend', __name__)


@frontend_page.route('/')
def index():
    return  render_template('index.html')


