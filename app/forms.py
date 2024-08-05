from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectMultipleField
from wtforms.validators import DataRequired
from wtforms.widgets import ListWidget, CheckboxInput
from app.models import Service

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class BookingForm(FlaskForm):
    client_name = StringField('Name', validators=[DataRequired()])
    date = HiddenField('Date', validators=[DataRequired()])  # Скрытое поле для даты
    time = HiddenField('Time', validators=[DataRequired()])
    service = MultiCheckboxField('Services', choices=[], coerce=int)  # Удален валидатор DataRequired
    submit = SubmitField('Book')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service.choices = [(service.id, f"{service.name} - ${service.price:.2f}") for service in Service.query.all()]
