from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,TextAreaField
# from wtforms.fields.html5 import EmailField or commonly use stringfield with email as validators
from wtforms.validators import (input_required,
                                Email,
                                length,
                                regexp,
                                optional,
                                EqualTo,
                                ValidationError
                                )

class MyFirstBasicForm(FlaskForm):
    Name=StringField("How do i call you!",validators=[input_required()])
    Email=StringField("Can i have your Email",validators=[Email(message="Please enter valid Email Address")])
    password=PasswordField("Password",validators=[length(min=8,max=16,message="Password must be 8-16 characters"),
                                            regexp(r"^[a-zA-Z0-9!@#$]+$",message="Regex failed")])
    confirmpassword=PasswordField("confirm password",validators=[EqualTo('password',message="Passwords are not matched")])

    def validate_Name(self,field):
        if(len(field.data)<5):
            raise ValidationError("Enter a name not a nickname with lesser charaters")

class postform(FlaskForm):
    title=StringField("Title of the Post",validators=[input_required()])
    description=TextAreaField("Description of the Post",validators=[input_required()])

    def validate_description(self,field):
        if len(field.data)<10:
            return ValidationError("Description is too short to post")
