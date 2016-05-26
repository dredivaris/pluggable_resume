
from flask import Flask

from flask_admin import Admin
from flask.ext.pymongo import PyMongo

from flask.ext.security import Security, login_required, \
  MongoEngineUserDatastore
from flask.ext.security import RoleMixin, UserMixin
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')
# app.secret_key = "super secret key"
# login_manager = LoginManager()
# login_manager.login_view = 'login'

mongo = PyMongo(app)
with app.app_context():
  db = mongo.db
# login_manager.init_app(app)

engine_db = MongoEngine(app)


class Role(engine_db.Document, RoleMixin):
    name = engine_db.StringField(max_length=80, unique=True)
    description = engine_db.StringField(max_length=255)


class User(engine_db.Document, UserMixin):
    email = engine_db.StringField(max_length=255)
    password = engine_db.StringField(max_length=255)
    active = engine_db.BooleanField(default=True)
    confirmed_at = engine_db.DateTimeField()
    roles = engine_db.ListField(engine_db.ReferenceField(Role), default=[])


admin = Admin(app, name='Admin', template_mode='bootstrap3', base_template='my_master.html')


from flask import render_template

# setup security
user_datastore = MongoEngineUserDatastore(engine_db, User, Role)
security = Security(app, user_datastore)


from wsgi.admin_views import *
from wsgi.resume_api import *


# route to flask tutorial page
@app.route('/')
def index():
    return render_template('index.html',
                           title='Home')


@app.route('/resume/')
@app.route('/resume/<url_specifier>/')
def resume(url_specifier=None):
    return render_template('live_resume.html',
                           title='Resume',
                           limited=True,
                           url_specifier=url_specifier)




