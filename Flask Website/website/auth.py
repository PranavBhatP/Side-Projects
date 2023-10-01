from flask import Blueprint, render_template, request, flash
email = ''
firstName = ''
password1 = ''
password2 = ''
auth = Blueprint('auth', __name__)


@auth.route('/login', methods =['GET', 'POST'])

def login():
    return render_template('login.html', boolean = True)

@auth.route('/logout')

def logout():
    return render_template('login.html')

@auth.route('/sign-up', methods  = ['GET', 'POST'])

def sign_up():
    email = None
    firstName = None
    password1 = None
    password2 = None
    if request.method == 'POST':
        
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

    if len(str(email)) < 4:# type: ignore
        flash("Email must be at least 4 characters", category= 'error')

    elif len(str(firstName)) < 2:# type: ignore
        flash("First name must be at least 2 characters", category= 'error')
    elif str(password1) != str(password2):# type: ignore
        flash("Password must be same as entered", category= 'error')
    elif len(str(password1)) < 8:# type: ignore
        flash("Password must be atleast 8 characters", category= 'error')
    else:
        flash("Account created successfully!", category= 'success')
    return render_template('sign_up.html')