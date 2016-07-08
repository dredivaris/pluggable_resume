from flask import render_template, Blueprint, make_response, request, abort
from user_agents import parse

from wsgi.models import ResumeSettings
from wsgi.resume_proxy import combined_resume

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
@frontend.route('/<url_specifier>/')
@frontend.route('/resume/')
@frontend.route('/resume/<url_specifier>/')
def resume(url_specifier=None):
    matching_specifier = False
    settings = ResumeSettings.objects.first()

    if url_specifier:
        if settings.enable_limited_resume and settings.limited_resume_url_specifier:
            if url_specifier == settings.limited_resume_url_specifier:
                matching_specifier = True

    if matching_specifier:
        combined_res = combined_resume(hide_work_experience=False)
    else:
        combined_res = combined_resume()

    if not combined_res:
        abort(404)

    user_agent = parse(request.user_agent.string)

    resp = make_response(render_template('live_resume.html',
                                         title=combined_res.title,
                                         resume=combined_res,
                                         looking_for=settings.looking_for,
                                         hide_basic_info=settings.hide_basic_info,
                                         resume_link=settings.resume_link,
                                         not_mobile=False if user_agent.is_mobile else True,
                                         url_specifier=url_specifier
                                            if matching_specifier else None,
                                         matching_specifier=matching_specifier))

    return resp

