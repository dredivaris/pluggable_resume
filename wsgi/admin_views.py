from flask import url_for, request
from flask.ext.admin.contrib import mongoengine
from flask.ext.login import current_user
from flask_admin import helpers as admin_helpers
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from wsgi.models import Resume, ResumeSettings
from wsgi.setup import admin, Role, User, security


class MyModelView(mongoengine.ModelView):
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


admin.add_view(MyModelView(Role))
admin.add_view(MyModelView(User))

admin.add_view(MyModelView(Resume))
admin.add_view(MyModelView(ResumeSettings))


# admin.add_view(UserView(db.user, 'User'))
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
    )