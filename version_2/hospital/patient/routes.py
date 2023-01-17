from hospital import app, db
from flask import render_template, request, session, flash, redirect, url_for
from .models import Patient
from .forms import RegistrationForm

@app.route("/patient/register", methods=['POST', 'GET'])
def register():
    if ("email" not in session) and (session.get("user_role") != 'Nurse'):
        flash(f'Unathorized', 'danger')
        return redirect(url_for('adminlogin'))
    form = RegistrationForm(request.form)
    if request.method == "POST":
        first_name = form.first_name.data
        last_name = form.last_name.data
        phoneNumber = form.phone.data
        sex = request.form.get('sex')
        status = request.form.get('status')
        email = form.email.data
        address = form.address.data
        city = form.city.data
        state = form.state.data
    
        emergencyName = form.Ename.data
        emergencyContact = form.Econtact.data
        relationship = form.relationship.data

        # print(f'first_name: {first_name} \n last_name: {last_name} \n phone: {phoneNumber} \n sex: {sex} \n status: {status} \n email: {email} \n address: {address} \n city: {city}\
        #  \n state: {state}  \n emergname: {emergencyName} \n emerCon: {emergencyContact} \n rela: {relationship}')

        user =Patient(first_name=first_name, last_name = last_name, phoneNumber=phoneNumber, sex=sex, status=status,  email=email, address=address, city=city,\
         state=state, emergencyName=emergencyName, emergencyContact=emergencyContact, relationship=relationship)
        db.session.add(user)
        db.session.commit()
        flash(f'User {first_name} Created Successfully', 'success')
        return redirect(url_for('patientRecord', id=user.id))

    return render_template('patient/register.html', title="Register Patient", form=form)


@app.route('/patient/record')
def patientRecord():
    """  """
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('adminlogin'))
    users = Patient.query.all()
    return render_template('patient/index.html', title='Patient record', users=users)

@app.route('/patient/record/<int:id>')
def patientDetailRecord(id):
    """  """
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('adminlogin'))
    user = Patient.query.get_or_404(id)
    return render_template('patient/full_details.html', title='Detail record', user=user)

@app.route('/patient/updatepatient/<int:id>', methods=["POST", "GET"])
def updatePatient(id):
    """Update Staff in the database"""
    if 'email' not in session or session.get('user_type') != 'Admin':
        flash(f'Please login first', 'danger')
        redirect(url_for('adminlogin'))
    form = RegistrationForm(request.form)
    users = Patient.query.get_or_404(id)

    if request.method == 'POST':
        users.first_name = form.first_name.data
        users.last_name = form.last_name.data
        users.phoneNumber = form.phone.data
        users.sex = request.form.get('sex')
        users.status = request.form.get('status')
        users.email = form.email.data
        users.address = form.address.data
        users.city = form.city.data
        users.state = form.state.data
    
        users.emergencyName = form.Ename.data
        users.emergencyContact = form.Econtact.data
        users.relationship = form.relationship.data

        db.session.commit()
        flash(f'Your users has been updated', 'success')
        return redirect(url_for('patientRecord'))

    form.first_name.data = users.first_name
    form.last_name.data = users.last_name
    form.phone.data = users.phoneNumber
    form.email.data = users.email
    form.address.data = users.address
    form.city.data = users.city
    form.state.data = users.state
    
    form.Ename.data = users.emergencyName 
    form.Econtact.data = users.emergencyContact
    form.relationship.data = users.relationship

    return render_template('admin/update_users.html', form=form, patient=users)


@app.route('/patient/deletepatient/<int:id>', methods=['POST'])
def deletePatient(id):
    """Delete Product from database"""
    if 'email' not in session or session.get('user_type') != 'Admin':
        flash(f'Please login')
        return redirect(url_for('adminlogin'))
    
    user = Patient.query.get_or_404(id)

    if request.method == 'POST':    
        db.session.delete(user)
        db.session.commit()
        flash(f'The User {user.first_name} was deleted from your database', 'success')
        return redirect(url_for('patientRecord'))
    flash(f'The product {user.first_name} can\'t be deleted', 'warning')
    return redirect(url_for("patientRecord"))



