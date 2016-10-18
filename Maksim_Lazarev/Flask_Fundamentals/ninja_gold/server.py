import random
import datetime
import time
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    if "balance" not in session:
        session['balance'] = 0
    if "activities" not in session:
            session['activities'] = ""
    return render_template('index.html')

@app.route("/process_money", methods=['POST'])
def process_money():
    tmp=0
    if request.form['button']=="farm":
         tmp=random.randint(10,20)
         session['balance'] += tmp
         session['activities'] += "<p class='green'>Earned "+str(tmp)+" golds from the farm! ("+str(time.strftime("%Y/%m/%d %I:%M %p")).lower()+")</p>"
    elif request.form['button']=="cave":
         tmp=random.randint(5,10)
         session['balance'] +=tmp
         session['activities'] += "<p class='green'>Earned "+str(tmp)+" golds from the farm! ("+str(time.strftime("%Y/%m/%d %I:%M %p")).lower()+")</p>"
    elif request.form['button']=="house":
         tmp=andom.randint(2,5)
         session['balance'] +=tmp
         session['activities'] += "<p class='green'>Earned "+str(tmp)+" golds from the farm! ("+str(time.strftime("%Y/%m/%d %I:%M %p")).lower()+")</p>"
    elif request.form['button']=="casino":
        tmp=random.randint(-50,50)
        session['balance'] +=tmp
        if (tmp>0):
            session['activities'] += "<p class='green'>Earned "+str(tmp)+" golds from the farm! ("+str(time.strftime("%Y/%m/%d %I:%M %p")).lower()+")</p>"
        else:
            session['activities'] += "<p class='red'>Entered a casino and lost "+str(-1*tmp)+" golds... Ouch.. ("+str(time.strftime("%Y/%m/%d %I:%M %p")).lower()+")</p>"
    return redirect('/')
app.run(debug=True)
