from flask import Flask, render_template, request, redirect, session
import random

def secretnumber():
    if "secret_number" not in session:
        session["secret_number"] = random.randrange(0, 101)

app = Flask(__name__)
app.secret_key= 'secretkey'

@app.route('/')
def home():
    secretnumber()
    return render_template('index.html')

@app.route('/guess', methods=['post'])
def guess():
    session['number'] = int(request.form['number'])
    return render_template('index.html', number=session['number'])

@app.route('/restart', methods=['post'])
def restart():
    if "secret_number" in session:
        session.pop('secret_number')
    secretnumber()
    return render_template('index.html')

app.run(debug=True)
