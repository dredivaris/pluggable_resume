from flask import render_template

from wsgi.__init__ import app


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