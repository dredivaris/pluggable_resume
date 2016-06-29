from flask import render_template, Blueprint, make_response
from wsgi.models import engine_db as db, Resume, ResumeSettings
from wsgi.resume_proxy import combined_resume

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
@frontend.route('/resume/')
@frontend.route('/resume/<url_specifier>/')
def resume(url_specifier=None):
    matching_specifier = False
    combined_res = None

    if url_specifier:
        settings = ResumeSettings.objects.first()
        if settings.enable_limited_resume and settings.limited_resume_url_specifier:
            if url_specifier == settings.limited_resume_url_specifier:
                matching_specifier = True

    if matching_specifier:
        combined_res = combined_resume(hide_work_experience=False)
    else:
        combined_res = combined_resume()
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    resp = make_response(render_template('live_resume.html',
                                         title=combined_res.title,
                                         resume=combined_res,
                                         url_specifier=url_specifier))
    resp.headers['X-Frame-Options'] = 'SAMEORIGIN, GOFORIT'
    return resp
