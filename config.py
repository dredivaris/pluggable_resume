import os

basedir = os.path.abspath(os.path.dirname(__file__))

MONGO_DBNAME = 'andreas_website'
SESSION_TYPE = 'mongodb'
SECRET_KEY = 'jkJKJGFDKJ*hG*&YD)JPSDGJLSKDJGOISUojidlsfkjasgd08adgpijG(HD('


# if os.environ.get('HEROKU') is None:
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