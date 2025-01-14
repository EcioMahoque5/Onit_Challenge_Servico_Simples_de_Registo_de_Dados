from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email, ValidationError


# Validators form to register the client
class ClientRegistrationForm(FlaskForm):
    first_name = StringField('first_name', validators=[
        DataRequired(message="First name is a required field!"), 
        Length(min=2, max=50, message="First name must have 2-50 characters!")])
    
    other_names = StringField('other_names', validators=[
        DataRequired(message="Other names is a required field!"), 
        Length(min=2, max=140, message="Other names must have 2-140 characters!")])
    
    email = StringField('email', validators=[
        DataRequired(message="Email is a required field!"), 
        Email(message="Email must be a valid email!"),
        Length(max=120, message="Email must have a max of 120 characters!")])
    
    address = StringField('address', validators=[
        DataRequired(message="Address is a required field!"), 
        Length(min=4, max=255, message="Address must have 4-255 characters!")])

    def __init__(self, *args, data_store=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_store = data_store or []

    def validate_email(self, field):
        if any(client['email'] == field.data for client in self.data_store):
            raise ValidationError('Email already registered.')
        