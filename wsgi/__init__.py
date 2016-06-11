from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.security import Security, MongoEngineUserDatastore
from flask_admin import Admin


app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

import sys
import logging
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

# app.secret_key = "super secret key"
# login_manager = LoginManager()
# login_manager.login_view = 'login'

# mongo = PyMongo(app)
# mongo = MongoClient(MONGO_URL + 'andreaswebsite')
# with app.app_context():
#   db = mongo.db
# login_manager.init_app(app)

engine_db = MongoEngine(app)


from wsgi.models import Role, User

admin = Admin(app, name='Admin', template_mode='bootstrap3', base_template='my_master.html')

# setup security
user_datastore = MongoEngineUserDatastore(engine_db, User, Role)
security = Security(app, user_datastore)

# route to flask tutorial page


from wsgi.admin_views import *
from wsgi.views import *
