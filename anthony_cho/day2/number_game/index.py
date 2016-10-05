from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# main page and counter
@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randrange(0, 101)
        print('random number generated')
    print("random number is", session['number'])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    session['user_guess'] = int(request.form['guess'])
    print("user guessed", session['user_guess'])
    return redirect('/')
@app.route('/replay', methods=['POST'])
def replay():
    session['number'] = random.randrange(0, 101)
    print('random number is ', session['number'])
    del session['user_guess']
    return redirect('/')
app.run(debug=True) # run our server
