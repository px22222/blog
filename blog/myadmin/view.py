from flask import (current_app, Blueprint, render_template,
                   abort, redirect, url_for, request)
from flask_security import  current_user
from flask_admin.contrib.sqla import ModelView


admin_page = Blueprint('admin_page', __name__)


@admin_page.route('/adminpage')
def hello_admin():
    return 'hello, admin'

class securemodelview(ModelView):
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
        return True

    def on_model_change(self, form, model, is_created):
        if is_created:
            print ('new table record is created')
        else:
            print ('table record is updated')

        return  super().on_model_change(form, model, is_created)




class entries_modelview(securemodelview):
    pass
