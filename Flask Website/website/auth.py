from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
#When we generate a hash, the hash generator will act like a function without an inverse function, so u will never be able to figure out what was the actual password after storing it in db.
from flask_login import login_user, login_required, logout_user, current_user
# email = ''
# firstName = ''
# password1 = ''
# password2 = ''
auth = Blueprint('auth', __name__)


@auth.route('/login', methods =['GET', 'POST'])

def login():
    # email = None
    # password = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user= User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category= 'success')
                login_user(user, remember = True)
                return redirect(url_for('views.home'))
            else:
                flash('Invalid password', category= 'error')

        else:
            flash('Email does not exist', category= 'error')
    return render_template('login.html', boolean = True)

@auth.route('/logout')
@login_required
def logout():
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods  = ['GET', 'POST'])

def sign_up():
    email = None
    first_name = None
    password1 = None
    password2 = None
    if request.method == 'POST':
        
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

    user= User.query.filter_by(email=email).first()
    if user:
        flash('Email already in use', category= 'error')
    if len(str(email)) < 4:
        flash("Email must be at least 4 characters", category= 'error')

    elif len(str(first_name)) < 2:
        flash("First name must be at least 2 characters", category= 'error')
    elif str(password1) != str(password2):# type: ignore
        flash("Password must be same as entered", category= 'error')
    elif len(str(password1)) < 8:
        flash("Password must be atleast 8 characters", category= 'error')
    else:
        new_user = User(email = email,first_name = first_name, password = generate_password_hash(password1, method ='sha256')) # type: ignore
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully!", category= 'success')
        return redirect(url_for('views.home'))
    
    return render_template('sign_up.html')