from hospital import app, db, bcrypt  
from flask import render_template, request, session, flash, redirect, url_for

from .forms import RegistrationForm, LoginForm
from .models import User


@app.route('/', methods=["Get"])
def home():
    return ("Welcome!")

@app.route('/admin/logout')
def logout():
    if 'email' in session:
        del session['email']
    return (redirect(url_for('home')))

@app.route('/admin/register', methods=["GET", 'POST'])
def admin():
    """ Registration Route For staff by admin """
    if 'email' not in session or session.get('user_type') != 'Admin':
        flash(f'Admins only!', 'danger')
        return redirect(url_for('adminlogin'))
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        # encrypt the form password
        hash_password = bcrypt.generate_password_hash(form.first_name.data)

        # print(last_name, first_name, password, email, address, phone, user_role, user_type)
        user = User(last_name = form.last_name.data,
                first_name = form.first_name.data,
                email = form.email.data,
                password = hash_password,
                address = form.address.data,
                phone = form.phone.data,
                user_type = request.form.get("user_type"),
                user_role = request.form.get("user_role"))
        db.session.add(user)
        db.session.commit()
<<<<<<< HEAD
        flash(f'Welcome {form.first_name.data} Thank you for registering', 'success')
        return redirect(url_for('adminPanel'))
    return render_template('admin/register.html', form=form, title='Register user')



@app.route('/admin/panel')
def adminPanel():
    """ Admin Panel to get all staff in database """
    if 'email' not in session or session.get('user_type') != 'Admin':
        flash(f'Admin Only!', 'danger')
        return redirect(url_for('adminlogin'))
    users = User.query.all()

    return render_template('admin/index.html', title='Admin Page', users=users)


@app.route('/admin/updatestaff/<int:id>', methods=["POST", "GET"])
def updateStaff(id):
    """Update Staff in the database"""
    if 'email' not in session or session.get('user_type') != 'Admin':
        flash(f'Admins only!', 'danger')
        redirect(url_for('adminlogin'))
    form = RegistrationForm(request.form)
    users = User.query.get_or_404(id)

    if request.method == 'POST':
        users.last_name = form.last_name.data
        users.first_name = form.first_name.data
        users.email = form.email.data
        users.address = form.address.data
        users.phone = form.phone.data
        users.user_type = request.form.get("user_type")
        users.user_role = request.form.get("user_role")
        

        db.session.commit()
        flash(f'Your users has been updated', 'success')
        return redirect(url_for('adminPanel'))

    
    form.last_name.data = users.last_name
    form.first_name.data = users.first_name
    form.email.data = users.email
    form.address.data = users.address
    form.phone.data = users.phone
    form.user_type.data = users.user_type
    form.user_role.data = users.user_role
    return render_template('admin/update_users.html', form=form, users=users)


@app.route('/admin/login', methods=['POST', 'GET'])
def adminlogin():
    """ Login Route """
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            session['user_type'] = user.user_type
            session['user_role'] = user.user_role
            session['id'] = user.id
            flash(f'Welcome {form.email.data} You are logedin as a user', 'success')
            return redirect(request.args.get('next') or url_for('home'))
        
        else:
            flash('Wrong Password or email try again', 'danger')
    return render_template('admin/login.html', form=form, title='Login Page')


@app.route('/deleteuser/<int:id>', methods=['POST'])
def deleteUser(id):
    """Delete User from database"""
    if 'email' not in session or session.get('user_tyep') != 'Admin':
        flash(f'Admins only!')
        return redirect(url_for('adminlogin'))
    
    user = User.query.get_or_404(id)

    if request.method == 'POST':    
        db.session.delete(user)
        db.session.commit()
        flash(f'The User {user.first_name} was deleted from your database', 'success')
        return redirect(url_for('adminPanel'))
    flash(f'The product {user.first_name} can\'t be deleted', 'warning')
    return redirect(url_for("adminPanel"))




=======
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

@app.route("/a/b", methods=["GET"])
def home():
    return("welcome")
>>>>>>> c4eb6165461deb8593c22321ecff4ec055c80795
