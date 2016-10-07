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
    print 'session: ',session
    if not 'mynum' in session:
        # show the guess form
        session['showform'] = True
    # create random number and add to session
        session['mynum'] = randint(0, 10000)
        print "Guess this!: ",session['mynum']
    else:
        session['showform'] = False
        print 'you guessed ',session['result']
        #reset the number in my head
        #session.pop('result')
        session.pop('mynum')


    return render_template("html/index.html")
# process guess
@app.route('/proc_guess',methods=['POST'])
def process_guess():
    session['showform'] = False
    session['result'] = 'correctly!' if session['mynum'] == int(request.form['guess']) else 'incorrectly!'

    return redirect('/')

app.run(debug=True)
