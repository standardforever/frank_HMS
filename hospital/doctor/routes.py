from hospital import app, db
from flask import render_template, request, session, flash, redirect, url_for
from .models import DoctorReport
from .forms import DoctorForm
from hospital.patient.models import Patient

@app.route("/doctor/createrecord/<int:id>", methods=['POST', 'GET'])
def createDoctorRecord(id):
    """Controller where doctor can create a record for patient"""
    if ("email" not in session) or (session.get("user_role") != 'Doctor'):
        flash(f'Unathorized', 'danger')
        return redirect(url_for('adminlogin'))
    form = DoctorForm(request.form)
    # patient = Patient.query.get_or_404(id)
    if request.method == "POST":
        entry = form.entry.data
        diagnosis = form.diagnosis.data
        recommendation = form.recommendation.data
        prescription = form.prescription.data
        doctor_id = session.get(id)
        patient_id = id
        # print(f'(entry={entry}, diagnosis={diagnosis}, prescription={prescription}, recommendation={recommendation}')

        report =DoctorReport(entry=entry, diagnosis=diagnosis, prescription=prescription,
                         recommendation=recommendation, doctor_id=id, patient_id=patient_id)
        db.session.add(report)
        db.session.commit()
        flash(f'Record created Successfully', 'success')
        return redirect(url_for('doctorAllRecord', id=id))

    return render_template('doctor/report.html', title="Create Record", form=form, id=id)


@app.route('/doctor/allrecord/<int:id>')
def doctorAllRecord(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('adminlogin'))
    records = Patient.query.get_or_404(id)
    return render_template('doctor/record.html', title='Doctor record', records=records.doctor_report, id=id)


