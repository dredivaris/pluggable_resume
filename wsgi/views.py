from flask import render_template, Blueprint

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return render_template('index.html',
                           title='Home')


@frontend.route('/resume/')
@frontend.route('/resume/<url_specifier>/')
def resume(url_specifier=None):
    return render_template('live_resume.html',
                           title='Resume',
                           limited=True,
                           url_specifier=url_specifier)