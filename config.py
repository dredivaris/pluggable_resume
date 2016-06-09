import os

basedir = os.path.abspath(os.path.dirname(__file__))

MONGODB_DB = 'andreas_website'
MONGO_DBNAME = 'andreaswebsite'

if os.environ.get('OPENSHIFT_MONGODB_DB_PASSWORD'):
    MONGODB_HOST = os.environ.get('OPENSHIFT_MONGODB_DB_HOST')
    MONGODB_PORT = int(os.environ.get('OPENSHIFT_MONGODB_DB_PORT'))
    MONGODB_USERNAME = os.environ.get('OPENSHIFT_MONGODB_DB_USERNAME')
    MONGODB_PASSWORD = os.environ.get('OPENSHIFT_MONGODB_DB_PASSWORD')
    MONGODB_DB = 'andreaswebsite'
    MONGO_DBNAME = 'andreaswebsite'

    MONGO_URL = os.environ.get('OPENSHIFT_MONGODB_DB_URL')
    SECRET_KEY = os.environ.get('OPENSHIFT_SECRET_TOKEN')
else:
    MONGODB_HOST = 'localhost'
    SESSION_TYPE = 'mongodb'
    SECRET_KEY = 'jkJKJGFDKJ*hG*&YD)JPSDGJLSKDJGOISUojidlsfkjasgd08adgpijG(HD('

SECURITY_URL_PREFIX = "/"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "IDHJG777D(*DGHJGKJDGHPJSDG*(J"

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "login/"
SECURITY_LOGOUT_URL = "logout/"
SECURITY_REGISTER_URL = "register/"

WTF_CSRF_ENABLED = False

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False

GOODREADS_DATABASE_NAME = 'Goodreads'

# if os.environ.get(º'HEROKU') is None:
#     SQLALCHEMY_DATABASE_URI = "postgresql://redditdbuser:redajisdg@localhost/redditclient"
# else:
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

'''mongo credentials:
   Root User:     admin
   Root Password: j22AkGKNvIMW
   Database Name: andreaswebsite
'''

# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')