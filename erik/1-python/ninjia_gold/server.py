from flask import Flask,render_template,request,redirect,session
import random
from random import randint

# the server is listening here
# localhost:5000/
app = Flask(__name__)
app.secret_key="OnlyInAJeep"
# default route
@app.route("/")
def index():
    if not 'total' in session:
        session['total'] = 0
    else:
        session['total'] += session['factor']

        #session.pop('log')

    if not 'log' in session:
        session['log']=[]
    else:
        #print ("add it to the log, baby",session['newentry'])
        #session['log'].append({'can be the same':'can also be the same'})
        session['log'].append(session['newentry'])
        #session.pop('newentry')

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
    # convert choice to a number
    session['factor']=getRand[session['choice']]

    print ("youre random allotment is:",session['factor'])
    print 'the button you clicked: ',session['choice']

    session['newentry'] = {'amount':session['factor'],'source':session['choice']}
    #session['newentry'] = {'amount':'the amount','source':'the source'}

    return redirect('/')

app.run(debug=True)
