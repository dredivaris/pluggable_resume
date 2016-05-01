
from flask.ext.admin.contrib.pymongo import ModelView

from wtforms import Form, StringField

class UserForm(Form):
    name = StringField('Name')
    email = StringField('Email')


class UserView(ModelView):
    column_list = ('name', 'email')
    form = UserForm
