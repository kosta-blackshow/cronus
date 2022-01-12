from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class OrderCheckForm(FlaskForm):
    order_id = order_id = StringField('Order ID', validators=[DataRequired()])
    check_order_id = SubmitField('Check exist in BIGRdb')


class AddCaseForm(FlaskForm):
    patient_id = StringField('Patient ID', validators=[DataRequired()])
    sex = SelectField('Sex', choices=[' ', 'F', 'M'], default=' ')
    submit = SubmitField('Add case')
