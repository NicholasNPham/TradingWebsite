from flask import Blueprint, render_template, request, flash

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
            flash('Account Created', category='success')

    return render_template("register.html")
