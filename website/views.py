from flask import Blueprint, render_template, request

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
        symbol = request.form.get('symbol')
        screener = request.form.get('screener')
        exchange = request.form.get('exchange')
        interval = request.form.get('interval')

        print(symbol)
        print(screener)
        print(exchange)
        print(interval)
    return render_template('analysis.html')