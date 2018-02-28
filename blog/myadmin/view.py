from flask import (current_app, Blueprint, render_template,
                   abort, redirect, url_for, request)
from flask_security import  current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose
from wtforms import TextAreaField
from wtforms.widgets import TextArea
import  datetime
from flask_admin.form import rules


admin_page = Blueprint('admin_page', __name__)


@admin_page.route('/adminpage')
def hello_admin():
    return 'hello, admin'


class BlogHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        print(current_user.is_active)
        if current_user.is_anonymous or not current_user.is_authenticated:
            return redirect(url_for('security.login', next=request.url))
        return  self.render('AdminIndex.html')

class SecureModelView(ModelView):
    can_create = True
    def is_accessible(self):
        print (current_user.is_active)
        if not current_user.is_active or not current_user.is_authenticated:
            print ('%s is not auth'  % current_user)
            return False
        return True


    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # redirect to login page
                return redirect(url_for('security.login', next=request.url))

    def is_visible(self):
        print (self.get_list_columns())
        return True

    def on_model_change(self, form, model, is_created):
        if is_created:
            print ('new table record is created')
        else:
            print ('table record is updated')

        return  super().on_model_change(form, model, is_created)


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor1'
        else:
            kwargs.setdefault('class', 'ckeditor1')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()



class EntriesModelView(SecureModelView):


    # form_excluded_columns = ['comment', ]
                             #'create_date', 'update_date']

    column_exclude_list = ['comment', 'content', 'plain_text']

    form_widget_args = {


        'plain_text':{
            'style': 'display: none',
        }
    }


    form_edit_rules = ['title','content', rules.Field('plain_text',
                                    render_field='lib.custom_render_field'),
                       'publish_status', 'allow_reply', 'stick', 'tags',
                       'category',]

    edit_template = 'entries_edit.html'


    #
    # extra_js = [ '/blog/admin/static/custom_js.js']

    form_overrides = {
        'content': CKTextAreaField
    }
    can_view_details = True

    def on_model_change(self, form, model, is_created):
        # if is_created:
        #     model.create_date = datetime.datetime.now()
        #     model.update_date = datetime.datetime.now()
        #
        # else:
        #     model.update_date = datetime.datetime.now()

        return super().on_model_change(form, model, is_created)


class CategoryModelView(SecureModelView):
    form_excluded_columns = ['entries']



class TagModelView(SecureModelView):
    form_excluded_columns = ['entries']


class CommentModelView(SecureModelView):
    form_excluded_columns = ['entries']


