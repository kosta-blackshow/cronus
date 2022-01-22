from flask import render_template, flash, redirect, url_for
from backend import server, db
from backend.forms import AddCaseForm, OrderCheckForm
from backend.models import Patient


@server.route('/', methods=['GET'])
def home():
    form = AddCaseForm()
    import_form = OrderCheckForm()
    return render_template(
        'add_case.html',
        form=form,
        import_form=import_form,
        order_title='Check Order ID',
        case_title='Firstly check order',
    )

@server.route('/import_order', methods=['POST'])
def import_order():
    form = AddCaseForm()
    import_form = OrderCheckForm()
    if import_form.check_order_id.data and import_form.validate_on_submit():
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

        #сгенерируй id
        patient = Patient()
        db.session.add(patient)
        db.session.flush()  # в этот момент происходит автогенерация id
        form.patient_id.data = f'CRONP-{patient.id:0>5}'
        db.session.rollback()
        db.session.close()
        flash('Patient ID is generated')

    return render_template(
        'add_case.html',
        form=form,
        import_form=import_form,
        order_title='Order ID',
        case_title='Add case to Cronus database',
    )


@server.route('/add_case', methods=['GET', 'POST'])
def add_case():
    form = AddCaseForm()
    import_form = OrderCheckForm()
    if form.submit.data and form.validate_on_submit(): # если все поля заполнены, то добавь в базу
        patient = Patient(
            patient=form.patient_id.data,
            sex=form.sex.data,
        )
        db.session.add(patient)
        db.session.commit()
        db.session.close()
        flash('Patient {} successfully added'.format(form.patient_id.data))

    return render_template(
        'add_case.html',
        form=form,
        import_form=import_form,
        order_title='Order ID',
        case_title='Add case to Cronus database',
    )