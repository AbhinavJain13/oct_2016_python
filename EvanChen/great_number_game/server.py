from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import random
def randomNumber():
    session['number'] = random.randrange(0,101)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guessNumber():
    session['guess'] = int(request.form['my_guess'])
    return redirect("/")

@app.route('/clear')
def newNumber():
   session['number'] = random.randrange(0,101)
   return redirect("/")

app.run(debug=True)
