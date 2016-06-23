from functools import wraps

from flask import jsonify
from flask.ext.restful import Api, Resource, reqparse, abort

# from app import app, db
# from app.models import User, FavoriteLink
# from app.reddit import get_submissions

from wsgi.resume_proxy import combined_resume

api = Api(prefix='/api/v1.0')  # Note, no app


class ReadingList(Resource):
    attribute = ''

    def get(self):
        resume = combined_resume()
        reading_list = [{'title': r.title, 'id': i}
                        for i, r in enumerate(getattr(resume.reading_list, self.attribute, None))]
    ***REMOVED***'success': True,
                'reading_list': reading_list}


class ReadingListCurrentlyReading(ReadingList):
    attribute = 'currently_reading'


class ReadingListFinishedReading(ReadingList):
    attribute = 'finished_reading'


class ReadingListFinishedReadingGeneral(ReadingList):
    attribute = 'finished_reading_general'


class ReadingListToRead(ReadingList):
    attribute = 'to_read'

api.add_resource(ReadingListCurrentlyReading, '/reading_list/currently_reading/')
api.add_resource(ReadingListFinishedReading, '/reading_list/finished_reading/')
api.add_resource(ReadingListFinishedReadingGeneral, '/reading_list/finished_reading_general/')
api.add_resource(ReadingListToRead, '/reading_list/to_read/')
