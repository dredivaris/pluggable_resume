from wsgi.views import db
from flask.ext.admin import BaseView, expose
from wsgi.models import UserView

from wsgi.views import admin


class MyView(BaseView):
  @expose('/')
  def index(self):
    return self.render('admin/woot.html')

admin.add_view(MyView(name='Woot'))
admin.add_view(UserView(db.user, 'User'))

