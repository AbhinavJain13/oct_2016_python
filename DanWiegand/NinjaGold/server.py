import random
import datetime
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'thisissecret'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = ""
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['action'] == 'farm':
        gold_added = random.randint(10,20)
        date = datetime.datetime.now()
        session['gold'] += gold_added
        session['activity'] += 'Earned {} gold from the farm! ({})'.format(str(gold_added), date)
    if request.form['action'] == 'cave':
        gold_added = random.randint(5,10)
        session['gold'] += gold_added
        date = datetime.datetime.now()
        session['activity'] += 'Earned {} gold from the cave! ({})'.format(str(gold_added), date)
    if request.form['action'] == 'house':
        gold_added = random.randint(2,5)
        session['gold'] += gold_added
        date = datetime.datetime.now()
        session['activity'] += 'Earned {} gold from the house! ({})'.format(str(gold_added), date)
    if request.form['action'] == 'casino':
        gold_added = random.randint(-50,50)
        session['gold'] += gold_added
        date = datetime.datetime.now()
        if gold_added > -1:
            session['activity'] += 'Earned {} gold from the casino! ({})'.format(str(gold_added), date)
        else:
            session['activity'] += 'Lost {} gold from the casino! ({})'.format(str(gold_added), date)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    print("Resetting game")
    del session['gold']
    del session['activity']
    return redirect('/')
app.run(debug=True)
