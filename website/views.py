from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/info')
def info():
    return "<h1>INFORMATION</h1>"

@views.route('/analysis')
def analysis():
    return "<h1>ANALYSIS</h1>"