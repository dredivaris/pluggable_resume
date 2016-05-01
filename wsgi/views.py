from flask import Flask
from flask_admin import Admin
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config.from_object('config')

mongo = PyMongo(app)
admin = Admin(app, name='andreas_website', template_mode='bootstrap3')
with app.app_context():
  db = mongo.db

from flask import render_template
# from wsgi import models, api


# route to flask tutorial page
@app.route('/')
def index():
    return render_template('index.html',
                           title='Home')


@app.route('/resume/')
def resume():
    return render_template('live_resume.html',
                           title='Resume')