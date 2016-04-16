from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from flask import render_template
from wsgi import models, api

# route to flask tutorial page
@app.route('/')
def index():
    return render_template('index.html',
                           title='Home')