from wtforms import StringField, IntegerField, Form
import wtforms.validators


class SearchForm(Form):
    q = StringField(validators=[wtforms.validators.Length(min=1, max=20)])
    page = IntegerField(validators=[wtforms.validators.NumberRange(min=1, max=99)], default=1)
