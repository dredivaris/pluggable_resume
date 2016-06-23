from flask import Flask
from flask.ext.security import Security, MongoEngineUserDatastore
from flask_admin import Admin
from flask_admin import helpers as admin_helpers

from wsgi.models import Resume, ResumeSettings, engine_db
from wsgi.filters import filters
from wsgi.views import frontend


admin = Admin(name='Admin', template_mode='bootstrap3', base_template='my_master.html')
security = Security()


def create_app(**config_overrides):
    global security
    app = Flask(__name__, template_folder='templates')
    app.config.from_object('config')
    app.config.update(config_overrides
                      )
    import sys
    import logging
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)
    engine_db.init_app(app)

    # setup security
    from wsgi import admin_views

    def security_context_processor():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=admin_helpers,
        )

    from wsgi.authentication_models import User, Role
    user_datastore = MongoEngineUserDatastore(engine_db, User, Role)
    security = Security(app)
    security._state = security.init_app(app, user_datastore)
    security.context_processor(security_context_processor)
    admin.init_app(app)

    app.register_blueprint(frontend)
    app.register_blueprint(filters)

    from wsgi.api import api
    api.init_app(app)

    return app

