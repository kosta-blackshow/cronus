from flask import render_template, flash, redirect, url_for
import sqlalchemy as sa
from backend import server, db
from backend.forms import (
    OrderCheckForm,
    CaseForm,
    AddCaseForm
)
from backend.models import Patient, Case, Biopsy, Sequence


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


@server.route("/table_patient", methods=["GET"])
def table_patient():
    patients = Patient.query
    return render_template("table_patient.html", patients=patients, title="Patient")


@server.route("/table_biopsy", methods=["GET"])
def table_biopsy():
    biopsies = Biopsy.query
    return render_template("table_biopsy.html", biopsies=biopsies, title="Biopsy")


@server.route("/table_sequence", methods=["GET"])
def table_sequence():
    sequences = Sequence.query
    return render_template("table_sequence.html", sequences=sequences, title="Sequence")


@server.route("/table_case", methods=["GET"])
def table_case():
    cases = Case.query
    return render_template("table_case.html", cases=cases, title="Case")


@server.route("/table_combined", methods=["GET"])
def table_combined():
    query = sa \
        .select([
        Case.id.label("case_id"),
        Patient.patient.label("patient_id"),
        Case.order_id,
        Biopsy.tumor_normal,
        Sequence.source,
        Biopsy.sample_storage_method,
        Biopsy.diagnosis_detailed,
        # Biopsy.tumor_content,
        # Biopsy.ploidy,
        # Biopsy.grade,
        Biopsy.t_stage,
        Biopsy.n_stage,
        Biopsy.m_stage,
        # Biopsy.stage,
        # Biopsy.dense_subtype,
        # Biopsy.MSI,
        # Biopsy.tumor_mutational_burden,
    ]) \
        .join(Patient, Case.patient) \
        .join(Sequence, Case.sequence) \
        .join(Biopsy, Sequence.biopsy) \
        .order_by(                       # сортировка и выбор строк
            Case.id.asc(),               # 1. чтобы образцы шли по порядку
            Biopsy.tumor_normal.desc(),  # 2. Tumor окажется выше Normal
            Sequence.source.asc()        # 3. DNA окажется выше RNA
    ) \
        .distinct(Case.id)               # 4. Выбирается единственная строка из возможных по case_id

    # таким образом строки выбираются по приоритету:
    # 1. Tumor biopsy and DNA sequencing
    # 2. Tumor RNA
    # 3. Normal DNA
    # 4. Normal RNA
    results = db.session.execute(query)
    return render_template("table_combined.html", results=results, title="Case")