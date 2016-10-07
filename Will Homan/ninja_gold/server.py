from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def landing_page():

    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def submit():
    if request.form['building'] == "farm":
        turngold = random.randint(10,20)
    elif request.form['building'] == "cave":
        turngold = random.randint(5,10)
    elif request.form['building'] == 'house':
        turngold = random.randint(2,5)
    elif request.form['building'] == 'casino':
        turngold = random.randint(-50,50)

    print('turngold is', turngold)
    print('activites is', session['activities'])
    if turngold < 0:
            string = "Entered a casino and lost " + str(turngold) + " golds....Ouch.","red"
            session['activities'].append(string)
    else:
            string = "Earned " + str(turngold) + " golds from the " + request.form['building'],"green"
            session['activities'].append(string)
    session['gold'] += turngold
    print("session gold is ", session['gold'])
    print("activities is", session['activities'])
    return redirect('/')


app.run(debug=True) # run our server
