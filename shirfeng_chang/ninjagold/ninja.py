import random, datetime
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if "gains" not in session:
        session["gains"] = 0
    if "activity" not in session:
        session["activity"] = ""
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
    places = {"farm": (10,20), "cave": (5,10), "house": (2,5), "casino": (-50,50)}
    session["gold"] = random.randint(places[request.form["building"]][0],places[request.form["building"]][1])

    if session["gold"] >= 0:
        session["activity"] += "Earned " + str(session["gold"]) + " gold from the " + request.form["building"] + "! " + str(datetime.datetime.now()) + "\n"
    else:
        session["activity"] += "Entered casino and lost " + str(session["gold"]) + " gold... Ouch. " + str(datetime.datetime.now()) + "\n"
    session["gains"]+= session["gold"]

    return redirect("/")
app.run(debug=True) # run our server
