from flask import render_template, Blueprint
from wsgi.models import engine_db as db, Resume, ResumeSettings
from wsgi.resume_proxy import combined_resume

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return render_template('index.html',
                           title='Home')


@frontend.route('/resume/')
@frontend.route('/resume/<url_specifier>/')
def resume(url_specifier=None):
    matching_specifier = False
    if url_specifier:
        settings = ResumeSettings.objects.first()
        if settings.enable_limited_resume and settings.limited_resume_url_specifier:
            if url_specifier == settings.limited_resume_url_specifier:
                matching_specifier = True

    if matching_specifier:
        resume = combined_resume(hide_work_experience=True)
    else:
        resume = combined_resume()

    return render_template('live_resume.html',
                           title=resume.title,
                           resume=resume,
                           limited=True,
                           url_specifier=url_specifier)
