from flask_wtf import Form
from wtforms import (StringField, PasswordField, BooleanField,
                    TextField, RadioField, SelectField, TextAreaField)
from wtforms.validators import (DataRequired, Email, Length, EqualTo)

# GLOBAL Variables
PROTEIN_CHOICES = [("C", "Chicken"), ("B", "Beef"), ("V", "Veggie"),
("N", "- none -")]
RICE_CHOICES = [("W", "White"), ("B", "Brown"), ("N", "- none -")]
BEAN_CHOICES = [("B", "Black"), ("P", "Pinto"), ("N", "- none-")]
SALSA_CHOICES = [("H", "Hot"), ("M", "Medium"), ("W", "Mild"),
("N", "- none -")]

class SignUp(Form):
    email = StringField(
        'Email', validators=[
        DataRequired(),
        Email()
        ])

    password = PasswordField(
    'Password', validators=[
    DataRequired(),
    EqualTo('password2', message="Passwords much match."),
    Length(min=5)
    ])

    password2 = PasswordField('Password2', validators=[])


class Login(Form):
    email = StringField(
        'Email', validators=[
        DataRequired(),
        Email()
        ])
    password = PasswordField(
        'Password', validators=[
        DataRequired()
        ])


class Burrito(Form):
    protein = SelectField("meat", choices=PROTEIN_CHOICES,
    validators=[DataRequired()
    ])
    rice = SelectField("rice", choices=RICE_CHOICES,
    validators=[DataRequired()
    ])
    bean = SelectField("bean", choices=BEAN_CHOICES,
    validators=[DataRequired()
    ])
    salsa = SelectField("salsa", choices=SALSA_CHOICES,
    validators=[DataRequired()
    ])

    cheese = BooleanField('cheese')
    sour_cream = BooleanField('sour cream')
    lettuce = BooleanField('lettuce')
    extras = TextAreaField('Additional Comments:')
