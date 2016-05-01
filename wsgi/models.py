from flask.ext.admin.contrib.pymongo import ModelView

from wtforms import Form, StringField

from wsgi.views import db, admin


class UserForm(Form):
    name = StringField('Name')
    email = StringField('Email')


class UserView(ModelView):
    column_list = ('name', 'email')
    form = UserForm


if __name__ == '__main__':
    # 'db' is PyMongo database object
    admin.add_view(UserView(db['users']))
