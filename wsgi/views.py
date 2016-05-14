from flask import Flask, request, flash, redirect, url_for
from flask.ext.login import LoginManager, login_user, logout_user, login_required
from flask_admin import Admin
from flask.ext.pymongo import PyMongo

from wsgi.forms import LoginForm
from wsgi.login import User

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "super secret key"
login_manager = LoginManager()
login_manager.login_view = 'login'

mongo = PyMongo(app)
with app.app_context():
  db = mongo.db
login_manager.init_app(app)

admin = Admin(app, name='Admin', template_mode='bootstrap3')

from flask import render_template


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print('woot got here')
    if request.method == 'POST' and form.validate_on_submit():
        user = db.users.find_one({"_id": form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj)
            flash("Logged in successfully!", category='success')
            return redirect(request.args.get("next") or url_for("write"))
        flash("Wrong username or password!", category='error')
    return render_template('login.html', title='login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


# route to flask tutorial page
@app.route('/')
@login_required
def index():
    return render_template('index.html',
                           title='Home')


@app.route('/resume/')
def resume():
    return render_template('live_resume.html',
                           title='Resume')


@login_manager.user_loader
def load_user(username):
    u = db.users.find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])
