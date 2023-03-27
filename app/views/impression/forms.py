from flask_wtf import FlaskForm
from wtforms.fields import FileField, SubmitField

class ImpressionForm(FlaskForm):
    impression_image = FileField()
    submit = SubmitField()