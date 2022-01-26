from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    SelectField,
    DateField,
    FloatField,
)
from wtforms.validators import DataRequired


class OrderCheckForm(FlaskForm):
    order_id = StringField("Order ID", validators=[DataRequired()])

    #def validate_order_id(self):
        #for patient in skip_empty_values_from_list_field(patients):
        #   if not s3_patient_exists(f"{form.cohort_id.data}/{patient}/", form.cloud_socket.data):
        #       raise ValidationError(f"Sample {patient} of cohort {form.cohort_id.data} not found on s3")
   #     pass
    check_order_id = SubmitField("Check exist in Cronus")


class CaseForm(FlaskForm):
    # patient information
    patient_id = StringField("Patient ID", validators=[DataRequired()])
    sex = SelectField("Sex", choices=[None, "F", "M"], default=None)
    date_of_birth = StringField("Date of birth")
    # biopsy information
    biopsy_id_1 = StringField("Biopsy ID")
    tumor_normal_1 = SelectField(
        "Tumor (T) of normal (N)",
        choices=[None, "T", "N"],
        default=None,
        validators=[DataRequired()],
    )
    sample_storage_method_1 = SelectField(
        "FF (F) or FFPE (P)",
        choices=[None, "F", "P"],
        default=None,
        validators=[DataRequired()],
    )
    biopsy_id_2 = StringField("Biopsy ID")
    tumor_normal_2 = SelectField(
        "Tumor (T) of normal (N)",
        choices=[None, "T", "N"],
        default=None,
        validators=[DataRequired()],
    )
    sample_storage_method_2 = SelectField(
        "FF (F) or FFPE (P)",
        choices=[None, "F", "P"],
        default=None,
        validators=[DataRequired()],
    )
    tumor_content = StringField("Tumor content")
    ploidy = StringField("Ploidy")
    grade = SelectField("Grade", choices=[None, "I", "II", "III", "IV"], default=None)
    t_stage = SelectField("T stage", choices=[None, "T0", "T1", "T2", "T3", "T4"], default=None)
    n_stage = SelectField("N stage", choices=[None, "N0", "N1", "N2", "N3", "N4"], default=None)
    m_stage = SelectField("M stage", choices=[None, "M0", "M1", "M2", "M3", "M4"], default=None)
    stage = SelectField("Clinical stage", choices=[None, "I", "II", "III", "IV"], default=None)
    diagnosis_detailed = StringField("Diagnosis Detailed")
    dense_subtype = StringField("Molecular functional portrait")
    MSI = SelectField("MSI status", choices=[None, "MSS", "MSI"], default=None)
    tumor_mutational_burden = StringField("Tumor mutational burden")
    # sequence information
    sequence_id_1 = StringField("Sequence ID")
    source_1 = SelectField("RNA (R) or DNA (D)", choices=[None, "R", "D"], default=None)
    sequence_id_2 = StringField("Sequence ID")
    source_2 = SelectField("RNA (R) or DNA (D)", choices=[None, "R", "D"], default=None)
    sequence_id_3 = StringField("Sequence ID")
    source_3 = SelectField("RNA (R) or DNA (D)", choices=[None, "R", "D"], default=None)
    # case information
    case_id = StringField("Case ID")
    order_id = StringField("Order ID", validators=[DataRequired()])


class AddCaseForm(CaseForm):
    submit = SubmitField("Add case")


class UpdateCaseForm(CaseForm):
    submit = SubmitField("Update case")

