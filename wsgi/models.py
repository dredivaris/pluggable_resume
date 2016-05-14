from flask.ext.admin.contrib.pymongo import ModelView
import flask.ext.login as login
from wtforms import Form, StringField, PasswordField


# class AuthenticatedModelView(ModelView):
#     def is_accessible(self):
#         return login.current_user.is_authenticated()


class UserForm(Form):
    name = StringField('Name')
    email = StringField('Email')
    password = PasswordField('password')


class UserView(ModelView):
    column_list = ('name', 'email', 'password')
    form = UserForm



