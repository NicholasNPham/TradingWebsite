from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route("/logout")
def logout():
    return "<p>LOGOUT</p>"

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be Greater than 3 Characters.', category='error')
        elif len(firstName) < 2:
            flash('Username must be Greater than 1 Characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not Match.', category='error')
        elif len(password1) < 7:
            flash('Password Must be at least 7 Characters', category='error')
        else:

            # Class Function for created new user to add to Database
            new_user = User(email=email,
                            firstName=firstName,
                            password= generate_password_hash(password1, method='sha256'))
            
            # Adding and Committing the New User into Database
            db.session.add(new_user)
            db.session.commit()
            
            flash('Account Created', category='success')

            # Redirect user to the Home Page
            return redirect(url_for('views.home'))

    return render_template("register.html")
