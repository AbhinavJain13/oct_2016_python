from flask import Flask, render_template, redirect, session, request
import random
import datetime

app = Flask(__name__)
app.secret_key = ('thisissecret')

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    buildings = {
        'farm': random.randint(10, 20),
        'cave': random.randint(5, 10),
        'house': random.randint(2, 5),
        'casino': random.randint(-50, 50),
    }
    date = datetime.datetime.now()
    print request.form
    #checking if the request is working by printing it to terminal
    print request.form['building']
    if request.form['building'] in buildings:
        print 'in if statement'
        gold_added = buildings[request.form['building']]
        session['gold'] += gold_added
        not_casino = "You earned {} gold from the {}!".format(gold_added, request.form['building'])
        casino = "You entered a casino and {} {} gold".format("won" if gold_added > 0 else "lost", gold_added if gold_added > 0 else -gold_added)
        print not_casino
        activity_content = {
            'activity': not_casino if request.form['building'] != 'casino' else casino,
            'date': date
        }
        session['activity'].append(activity_content)
        print session['activity']
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')
    





app.run(debug = True)
