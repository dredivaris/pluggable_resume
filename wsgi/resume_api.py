import json
from functools import wraps
import jsonpickle

from flask import jsonify, request
from flask.ext.restful import Api, Resource, reqparse, abort
from flask.ext.security import auth_token_required

from wsgi.exceptions import InvalidDataException
from wsgi.models import *

resume_api = Api(prefix='/api/v1.0')


def process_resume_object(data):
    linkedin_resume = jsonpickle.decode(data)

    resume = Resume.objects.filter(is_primary=False)[0]

    resume.name = linkedin_resume.name
    resume.headline = linkedin_resume.headline
    resume.industry = linkedin_resume.industry
    resume.connections = linkedin_resume.connections
    resume.title = 'linkedin resume'

    resume.basic_info = BasicInfo(industry=resume.industry, location=linkedin_resume.locality)
    resume.summary_info = SummaryInfo(
        summary=linkedin_resume.summary_info.summary,
        current_position=linkedin_resume.summary_info.current_position,
        previous_positions=linkedin_resume.summary_info.previous_position)

    # existing_top_skills = list(resume.top_skills)
    # existing_other_skills = list(resume.other_skills)
    existing_skills = resume.skills

    top_skills = \
        [Skill(name=top_skill.name, url=top_skill.url) for top_skill in linkedin_resume.top_skills]

    other_skills = \
        [Skill(name=other_skill.name, url=other_skill.url) for
         other_skill in linkedin_resume.other_skills]

    # decided to combine all skills in resume
    skills = top_skills + other_skills

    def overwrite_level(skills_to_overwrite, skills_to_check):
        for skill in skills_to_overwrite:
            skill.skill_level = 0
            for other_skill in skills_to_check:
                if skill.name == other_skill.name:
                    skill.skill_level = other_skill.skill_level
                    skill.order_by = other_skill.order_by
    overwrite_level(skills, existing_skills)

    resume.skills = skills

    resume.work_experiences = \
        [Experience(company_title=ex.company_title,
                    position_location=ex.position_location,
                    company_url=ex.company_url,
                    time_at_position=ex.time_at_position,
                    position_title_url=ex.position_title_url,
                    position_title=ex.position_title,
                    company_image_url=ex.company_image_url,
                    from_date=ex.from_date,
                    to_date=ex.to_date,
                    description=ex.description) for ex in linkedin_resume.experiences]

    resume.certifications = \
        [Certification(title=c.title,
                       license=c.license,
                       issuer_url_or_certificate_url=c.issuer_url_or_certificate_url,
                       issuer_url=c.issuer_url,
                       date=c.date,
                       issuer_image_url=c.issuer_image_url,
                       cert_url=c.cert_url,
                       institution=c.institution) for c in linkedin_resume.certifications]

    resume.schools = \
        [School(name=s.name,
                image=s.image,
                to_date=s.to_date,
                from_date=s.from_date,
                degree=s.degree,
                url=s.url) for s in linkedin_resume.schools]

    resume.languages = \
        [Language(name=l.name,
                  proficiency_level=l.proficiency_level) for l in linkedin_resume.languages]

    resume.save()
    return str(resume.id)


class ResumeAPI(Resource):
    decorators = [auth_token_required]

    def post(self):
        print('in post processing resume from linkedin')
        error = None
        json_data = request.get_json(force=True)
        try:
            obj_id = process_resume_object(json_data['data'])
        except InvalidDataException:
            error = 'Invalid resume json object'

    ***REMOVED***'success': False, 'error: ': error} if error else {'success': True, 'id': obj_id}

resume_api.add_resource(ResumeAPI, '/resume/')

