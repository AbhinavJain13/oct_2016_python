from flask import Flask, render_template, redirect, request, session
from random import randint
import time

app = Flask(__name__)
app.secret_key = "Secret_KEY"  # take care of sensative information learn to encrypt later

@app.route('/')      
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])     # server to host the farm field process money because thats in written instructions, also name of the page of the route
def process():
    data = {"farm": randint(10,20), "cave":randint(5,10), "house":randint(2,5), "casino":randint(-50,50)} #collecting a dictionary of output for each item.
    building = request.form['building']        #pull the info from the html
    gold = data[building]
    now = time.strftime("%Y-%m-%d %I:%M:%S %p") #time function
    act = {}  #will fill upon users session
    if gold > 0:
        act = {"status":"earn", "log":"Earned {} golds from the {}! ({})".format(gold, building, now)}  # the order in which goes inside each {} is in formats (1 ,2 ,3 ) ex. = {1:rules}..
    elif gold < 0:
        act = {"status":"lost", "log":"Entered a casino and lost {} golds... Ouch.. ({})".format(-gold, now)}
    else:
        act = {"status":"null", "log":"Entered a casino and got nothing... ({})".format(now)}       # different outcomes of golds variable
    session['gold'] += gold     # now lets show them what they got
    session['activity'].append(act) # and show the activity log
    return redirect('/')

@app.route('/reset')    # user wants to play again? lets let them
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
