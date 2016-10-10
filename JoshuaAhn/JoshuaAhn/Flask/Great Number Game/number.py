from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of number.py below

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randrange(1, 101)
        print('Okay Ready to Start')
    print("random number is", session['number'])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    session['userguess'] = int(request.form['guess'])
    print("Got the guess", session['userguess'])
    return redirect('/')

@app.route('/replay', methods=['POST'])
def replay():
    session['number'] = random.randrange(0, 101)
    print('My number is ', session['number'])
    del session['userguess']
    return redirect('/')
app.run(debug=True) # debug mode running
