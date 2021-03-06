from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password')
