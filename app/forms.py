# coding=utf-8;

from flask_wtf import Form
from wtforms import StringField, IntegerField, FileField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError

GENDER = {
    '0': 'male',
    '1': 'female'
}

GENDER_CHOICES = list((k, v) for k, v in GENDER.iteritems())


def _int_required(form, field):
    try:
        int(field.data)
    except ValueError:
        raise ValidationError('Integer value required')


class ProfileForm(Form):
    username = StringField('Username', validators=[InputRequired(),
                                                   Length(max=80)])
    first_name = StringField('First name', validators=[InputRequired(),
                                                       Length(max=80)])
    last_name = StringField('Last name', validators=[InputRequired(),
                                                     Length(max=80)])
    age = IntegerField('Age', validators=[InputRequired()])
    gender = SelectField('Gender', choices=GENDER_CHOICES, validators=[])
    image = FileField('Profile image', validators=[InputRequired()])