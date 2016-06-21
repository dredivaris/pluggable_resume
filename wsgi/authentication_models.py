from flask.ext.security import RoleMixin, UserMixin

from wsgi import engine_db


class Role(engine_db.Document, RoleMixin):
    name = engine_db.StringField(max_length=80, unique=True)
    description = engine_db.StringField(max_length=255)


class User(engine_db.Document, UserMixin):
    email = engine_db.StringField(max_length=255)
    password = engine_db.StringField(max_length=255)
    active = engine_db.BooleanField(default=True)
    confirmed_at = engine_db.DateTimeField()
    roles = engine_db.ListField(engine_db.ReferenceField(Role), default=[])