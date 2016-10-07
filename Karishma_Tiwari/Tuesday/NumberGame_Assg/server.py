from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if "number" not in session:
        session["number"]=random.randrange(0,101)


    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def onGuess():
    session["guess"]= int(request.form["guess"])
    return redirect('/')

@app.route("/reset", methods=["POST"])
def onClick():

    if "number" in session:
        session.pop("number")
        return redirect('/')

app.run(debug = True)
