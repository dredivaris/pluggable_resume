import json
from functools import wraps
import jsonpickle

from flask import jsonify, request
from flask.ext.restful import Api, Resource, reqparse, abort
from flask.ext.security import auth_token_required

from wsgi.api_exceptions import InvalidDataException
from wsgi.views import app, db

api = Api(app)


def process_resume_object(data):
    print('here we go?')
    print('received: ', data)
    linkedin_resume = jsonpickle.decode(data)
    print(type(linkedin_resume))


class ResumeAPI(Resource):
    decorators = [auth_token_required]

    def post(self):
        error = None
        json_data = request.get_json(force=True)
        try:
            resume_id = json_data['resume_id']
        except KeyError:
            error = 'missing resume_id'
        print('resume id ', resume_id)
        try:
            process_resume_object(json_data['data'])
        except InvalidDataException:
            error = 'Invalid resume json object'
        return {'success': True}


api.add_resource(ResumeAPI, '/resume/api/v1.0/')

