from flask import redirect, request
from flask import url_for, abort
from flask_admin.contrib import mongoengine

from flask_security import current_user


# class UserForm(Form):
#   username = StringField('Username')
#   name = StringField('Name')
#   email = StringField('Email')
#   password = PasswordField('New Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#   confirm = PasswordField('Repeat Password', [validators.DataRequired()])
#
#
# class UserView(ModelView):
#   column_list = ('_id', 'name', 'email')
#   form = UserForm


class MyModelView(mongoengine.ModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
    ***REMOVED***
        Override builtin _handle_view in order to redirect users when a view is not accessible.
    ***REMOVED***
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
    ***REMOVED***
                # login
                return redirect(url_for('security.login', next=request.url))
