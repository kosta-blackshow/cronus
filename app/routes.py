from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import AddCaseForm, OrderCheckForm
from app.models import Patient

@app.route('/', methods=['GET', 'POST'])
@app.route('/add_case', methods=['GET', 'POST'])
def add_case():
    add_form = AddCaseForm()
    check_form = OrderCheckForm()
    if check_form.check_order_id.data and check_form.validate_on_submit():
        check_form = OrderCheckForm(**{'order_id': check_form.order_id.data})
        #сгенерируй id
        patient = Patient()
        db.session.add(patient)
        db.session.flush()  # в этот момент происходит автогенерация id
        add_form.patient_id.data = f'BIGRP-{patient.id:0>5}'
        flash('Patient ID is generated')

    if add_form.submit.data and add_form.validate_on_submit(): # если все поля заполнены, то добавь в базу
        patient = Patient(
            patient=add_form.patient_id.data,
            sex=add_form.sex.data,
        )
        db.session.add(patient)
        db.session.commit()
        flash('Patient {} successfully added'.format(add_form.patient_id.data))

    return render_template(
        'add_case.html',
        add_form=add_form,
        check_form=check_form,
    )

#@app.route('/add_case_to_patient')
#def