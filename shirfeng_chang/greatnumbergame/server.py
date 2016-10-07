import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if "secret" not in session:
        session["secret"] = random.randrange(0,101)
    return render_template("index.html")

@app.route('/try',methods=['POST'])
def guess():
    session["guess"] = int(request.form["guess"])
    return redirect('/')

@app.route('/correct',methods=['POST'])
def correct():
    session["secret"] = random.randrange(0,101)
    del session["guess"]
    return redirect('/')

app.run(debug=True)
