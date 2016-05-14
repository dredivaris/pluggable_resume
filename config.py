import os

basedir = os.path.abspath(os.path.dirname(__file__))

MONGO_DBNAME = 'andreas_website'
MONGODB_DB = 'andreas_website'
MONGODB_HOST = 'localhost'
SESSION_TYPE = 'mongodb'
SECRET_KEY = 'jkJKJGFDKJ*hG*&YD)JPSDGJLSKDJGOISUojidlsfkjasgd08adgpijG(HD('

SECURITY_URL_PREFIX = "/"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "IDHJG777D(*DGHJGKJDGHPJSDG*(J"


# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False

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