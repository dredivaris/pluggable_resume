# class UserForm(Form):
#   username = StringField('Username')
#   name = StringField('Name')
#   email = StringField('Email')
#   password = PasswordField('New Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#   confirm = PasswordField('Repeat Password', [validators.DataRequired()])
#
#
# class UserView(ModelView):
#   column_list = ('_id', 'name', 'email')
#   form = UserForm



