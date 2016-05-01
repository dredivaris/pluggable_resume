from wsgi.views import db
from flask.ext.admin import BaseView, expose
from wsgi.models import UserView

from wsgi.views import admin


class MyView(BaseView):
  @expose('/')
  def index(self):
    print('in admin index')
    return self.render('admin/woot.html')

print('adding admin views')
admin.add_view(MyView(name='Woot'))
admin.add_view(UserView(db.user, 'User'))

