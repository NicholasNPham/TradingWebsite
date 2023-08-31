from flask import Blueprint, render_template, request, flash
from analysis import analysisForm
from flask_login import login_required, current_user
from .models import Note
from . import db

# Pandas Module Reading Excel Sheet
import pandas as pd

excelData = pd.read_excel('StockForex.xlsx')

tickers = excelData['Symbol'].tolist()
locations = excelData['Screener'].tolist()

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
             new_note = Note(data=note, user_id=current_user.id)
             db.session.add(new_note)
             db.session.commit()
             flash('Note Added', category='success')

    return render_template('home.html', user=current_user)

@views.route('/info')
def info():
    return render_template('info.html', user=current_user)

@views.route('/analysis', methods=['GET', 'POST'])
def analysis():
    if request.method == 'POST':
        symbol = str(request.form.get('symbol'))
        screener = str(request.form.get('screener'))
        exchange = str(request.form.get('exchange'))
        interval = str(request.form.get('interval'))
        analysisType = str(request.form.get('analysis'))
        print(analysisType)

        # Checks to see if symbol is in SPX500 Stock List congruent to Excel Sheet.
        if symbol not in tickers:
            flash('Symbol Not Found! Only S&P500 Stocks', category='error')
        elif screener not in locations: # Checks if screener is found in the Excel Sheet
            flash('Screener Not Found. Please Try Again!') 
        else:
            analysis = analysisForm(symbol=symbol,
                                    screener=screener,
                                    exchange=exchange,
                                    interval=interval,
                                    analysisType=analysisType)
        
            flash(analysis, category='success')

    return render_template('analysis.html', user=current_user)