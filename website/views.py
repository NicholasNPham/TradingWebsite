from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>HOME</h1>"

@views.route('/info')
def info():
    return "<h1>INFORMATION</h1>"

@views.route('/analysis')
def analysis():
    return "<h1>ANALYSIS</h1>"