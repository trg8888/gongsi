from wtforms import Form,BooleanField,StringField,validators

class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=4,max=25)])
    email = StringField('Emain Address', [validators.Length(min=6, max=35)])
    password = StringField('password', [validators.Length(min=6, max=35)])