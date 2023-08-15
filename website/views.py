from flask import Blueprint, render_template, request, flash
from analysis import analysisForm

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/info')
def info():
    return render_template('info.html')

@views.route('/analysis', methods=['GET', 'POST'])
def analysis():
    if request.method == 'POST':
        symbol = str(request.form.get('symbol'))
        screener = str(request.form.get('screener'))
        exchange = str(request.form.get('exchange'))
        interval = str(request.form.get('interval'))

        analysis = analysisForm(symbol=symbol,
                                screener=screener,
                                exchange=exchange,
                                interval=interval)
        
        flash(analysis, category='success')

    return render_template('analysis.html')