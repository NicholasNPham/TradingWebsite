from flask import Blueprint, render_template, request

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

        if len(email) > 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        else:
            pass

    return render_template("register.html")
