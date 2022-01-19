from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class OrderCheckForm(FlaskForm):
    order_id = StringField('Order ID', validators=[DataRequired()])

    #def validate_order_id(self):
        #for patient in skip_empty_values_from_list_field(patients):
        #   if not s3_patient_exists(f"{form.cohort_id.data}/{patient}/", form.cloud_socket.data):
        #       raise ValidationError(f'Sample {patient} of cohort {form.cohort_id.data} not found on s3')
   #     pass
    check_order_id = SubmitField('Check exist in BIGRdb')


class CaseForm(FlaskForm):
    patient_id = StringField('Patient ID', validators=[DataRequired()])
    sex = SelectField('Sex', choices=[' ', 'F', 'M'], default=' ')


class AddCaseForm(CaseForm):
    submit = SubmitField('Add case')


class UpdateCaseForm(CaseForm):
    update = SubmitField('Update case')
