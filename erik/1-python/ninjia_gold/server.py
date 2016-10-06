from flask import Flask,render_template,request,redirect,session,flash
import datetime
import time
import random
from random import randint

# the server is listening here
# localhost:5000/
app = Flask(__name__)
app.secret_key="OnlyInAJeep"
# default route
@app.route("/")
def index():
    # CREATE OR ADD TO THE TOTAL
    if not 'total' in session:
        session['total'] = 0
    else:
        session['total'] += session['factor']
    # CREATE OR ADD TO THE LOG
    if not 'log' in session:
        print "There was no log, so one was created for you."
        session['log']=[]
    else:
        session['log'].insert(0,session['newentry'])
        #session.pop('log') USE TO RESET LOG

    return render_template("html/index.html")

# process guess
@app.route('/proc_gold',methods=['POST'])
def process_guess():

    getRand = {
        'farm':randint(10,20),
        'cave':randint(5,10),
        'house':randint(2,5),
        'casino':randint(-50,50)
    }

    #which button was pushed?
    if 'farm' in request.form:
        session['choice']='farm'
    elif 'cave' in request.form:
        session['choice']='cave'
    elif 'house' in request.form:
        session['choice'] = 'house'
    else:
        session['choice'] = 'casino'

    # ADDING VALIDATION
    # if len(session['choice']) <1:
    #     flash("Enter a value, please.")
    # else:
    #     flash("Success! Your name is {}".format(request.form['factor']))

    # convert choice to a number via getRand dictionary...
    session['factor']=getRand[session['choice']]
    # create the log entry
    session['newentry'] = {'amount':session['factor'],'source':session['choice'],'when':datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')}

    return redirect('/')

app.run(debug=True)
