from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)
app.secret_key= 'secretkey'

@app.route('/')
def home():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = ""
    return render_template('index.html')

@app.route('/process_money', methods=['post'])
def getmoney():
    if request.form['action'] == 'farm':
        gold_added = random.randint(10,20)
        date = datetime.datetime.now()
        session['gold'] += gold_added
        session['activity'] += 'Earned {} gold from the farm! ({})'.format(str(gold_added), date)
        print(session['activity'])
        print('farmed')
    if request.form['action'] == 'cave':
        gold_added = random.randint(5,10)
        session['gold'] += gold_added
        date = datetime.datetime.now()
        session['activity'] += 'Earned {} gold from the cave! ({})'.format(str(gold_added), date)
        print('caved')
    if request.form['action'] == 'house':
        gold_added = random.randint(2,5)
        session['gold'] += gold_added
        date = datetime.datetime.now()
        session['activity'] += 'Earned {} gold from the house! ({})'.format(str(gold_added), date)
        print('housed')
    if request.form['action'] == 'casino':
        plus_or_minus = random.randint(1,2)
        if plus_or_minus == 1:
            gold_added = random.randint(0,50)
            session['gold'] += gold_added
            date = datetime.datetime.now()
            session['activity'] += 'Earned {} gold from the casino! ({})'.format(str(gold_added), date)
        else:
            gold_removed = random.randint(0,50)
            session['gold'] -= gold_removed
            date = datetime.datetime.now()
            session['activity'] -= 'Lost {} gold from the casino. Sorry bruh! ({})'.format(str(gold_removed), date)
        date = datetime.datetime.now()
        print('casino')
    session['activity'] += "\n"
    return redirect('/')

app.run(debug=True)
