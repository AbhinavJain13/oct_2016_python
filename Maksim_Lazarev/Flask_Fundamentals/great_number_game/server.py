import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if "rndNum" not in session:
        session['rndNum'] = random.randint(1,101)
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def result():
    if request.form['action'] == 'play':
        if (request.form['number']):
            session['userNum'] = int(request.form['number'])
        return redirect('/')
    elif request.form['action'] == 'reset':
        session.clear()
    return redirect('/')
app.run(debug=True)
