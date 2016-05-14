
from wsgi.models import MyModelView
from flask.ext.admin import BaseView, expose
from flask_admin import helpers as admin_helpers
from flask.ext.security import login_required


from wsgi.views import admin, Role, User, engine_db, security

class MyView(BaseView):
    @expose('/')
    @login_required
    def index(self):
        return self.render('admin/woot.html')

admin.add_view(MyView(name='Woot'))
admin.add_view(MyModelView(Role, engine_db))
admin.add_view(MyModelView(User, engine_db))

# admin.add_view(UserView(db.user, 'User'))
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
    )