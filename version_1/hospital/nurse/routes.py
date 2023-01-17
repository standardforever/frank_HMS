from hospital import app, db
from flask import render_template, request, session, flash, redirect, url_for
from .models import NurseReport
from .forms import NurseForm
from hospital.patient.models import Patient

@app.route("/nurse/createrecord/<int:id>", methods=['POST', 'GET'])
def createNurseRecord(id):
    if ("email" not in session) or (session.get("user_role") != 'Nurse'):
        flash(f'Unathorized', 'danger')
        return redirect(url_for('adminlogin'))
    form = NurseForm(request.form)
    # patient = Patient.query.get_or_404(id)
    if request.method == "POST":
        entry = form.entry.data
        temperature = form.temperature.data
        weight = form.weight.data
        blood_pressure = form.blood_pressure.data

        # print(f'(entry={entry}, temperature={temperature}, weight={weight}, blood_pressure={blood_pressure}')

        report =NurseReport(entry=entry, temperature=temperature, weight=weight, blood_pressure=blood_pressure,
                    patient_id=id, nurse_id=session.get('id'))

        db.session.add(report)
        db.session.commit()
        flash(f'Record created Successfully', 'success')
        return redirect(url_for('nurseAllRecord', id=id))
    print(id)
    return render_template('nurse/report.html', title="Create Record", id=id, form=form)



@app.route('/nurse/allrecord/<int:id>', methods=['GET'])
def nurseAllRecord(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('adminlogin'))
    records = Patient.query.get_or_404(id)
    return render_template('nurse/record.html', title='Nurse record', records=records.nurse_report, id=id)


