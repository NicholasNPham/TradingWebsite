from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '<p>LOGIN</p>'

@auth.route('/logout')
def logout():
    return '<p>LOGOUT</p>'

@auth.route('/register')
def register():
    return '<p>REGISTER</p>'