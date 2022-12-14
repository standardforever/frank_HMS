from hospital import app, db
from flask import render_template, request, session, flash, redirect, url_for
from .models import User

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        phoneNumber = request.form.get('phoneNumber')
        sex = request.form.get('sex')
        status = request.form.get('status')
        email = request.form.get('email')
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        weight = request.form.get('weight')
        height = request.form.get('height')
        medication = request.form.get('medication')
        if medication == 'True':
            medication = True
        else:
            medication = False
        message = request.form.get('message')
        emergencyName = request.form.get('emergencyName')
        emergencyContact = request.form.get('emergencyContact')
        relationship = request.form.get('name')
        user =User(name=name, phoneNumber=phoneNumber, sex=sex, status=status,  email=email, address=address, city=city,\
         state=state, weight=weight, height=height, medication=medication, message=message,\
          emergencyName=emergencyName, emergencyContact=emergencyContact, relationship=relationship)
        db.session.add(user)
        db.session.commit()
        flash(f'User {name} Created Successfully', 'success')
        return redirect(url_for('login'))

        # print(f'name: {name} \n phone: {phoneNumber} \n sex: {sex} \n status: {status} \n email: {email} \n address: {address} \n city: {city}\
        #  state: {state} \n weight: {weight} \n height: {height} \n medication: {medication} \n message: {message}\
        #   \n emergname: {emergencyName} \n emerCon: {emergencyContact} \n rela: {relationship}')

    return render_template('admin/register.html', register='register')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('name')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        print(user)
    return render_template('admin/login.html', login='login')
