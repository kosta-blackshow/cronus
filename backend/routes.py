from flask import render_template, flash, redirect, url_for
from backend import server, db
from backend.forms import (
    OrderCheckForm,
    CaseForm,
    AddCaseForm,
    UpdateCaseForm,
)
from backend.models import Patient, Case


@server.route("/", methods=["GET"])
@server.route("/index", methods=["GET"])
def index():
    order_check_form = OrderCheckForm()
    form = CaseForm()
    return render_template(
        "check.html",
        order_check_form=order_check_form,
        form=form,
    )

@server.route("/import_order", methods=["POST"])
def import_order():
    form = AddCaseForm()
    order_check_form = OrderCheckForm()
    if order_check_form.check_order_id.data and order_check_form.validate_on_submit():
        # 1 - проверка есть ли ордер в базе данных
        # если да - вернуть все данные пациента и кейса
        #         - создать и заполнить форму UpdateCaseFom
        # иначе -
        # 2 - проверка, есть ли данные на s3
        # если да - создать нового пациента
        #         - попробовать подгрузить данные из Йорма
        #         - создать и заполнить форму AddCaseForm
        # иначе - вызвать ошибку, что фалов нет на s3
        #       - перенаправить на начальную страницу

        # generate patient id
        last_patient = Patient.query.order_by(-Patient.id).first()
        if last_patient is None: # if table Patient is empty
            last_id = 0
        else:
            last_id = last_patient.id
        form.patient_id.data = f"CRONP-{last_id+1:0>5}"
        flash(f"Patient ID is generated: {form.patient_id.data}")

    return render_template("add.html", form=form)


@server.route("/add_case", methods=["POST"])
def add_case():
    form = AddCaseForm()
    if form.submit.data and form.validate_on_submit(): # если все поля заполнены, то добавь в базу
        patient = Patient(
            patient=form.patient_id.data,
            sex=form.sex.data,
            date_of_birth=form.date_of_birth.data
        )

        db.session.add(patient)
        db.session.commit()

        form.patient_id.data = patient.patient
        flash(f"Patient {form.patient_id.data} successfully added")
        return redirect('/')

    return render_template('add.html', form=form)

@server.route("/patient_table", methods=["GET"])
def patient_table():
    patients = Patient.query
    return render_template("patients_table.html", patients=patients)