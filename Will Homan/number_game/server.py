from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')

def landing_page():

    if 'secretnum' not in session:
        session['secretnum'] = random.randrange(0, 101)
        print("secret num is ", session['secretnum'])
    return render_template('index.html')


@app.route('/numguess', methods=['POST'])
def submit():

        if 'guess' not in session:
            session['guess'] = 0

        session['guess'] = int(request.form['guess'])
        print("guess is ", session['guess'])
        print("secret num is ", session['secretnum'])
        return redirect('/')

@app.route('/reset', methods=['POST'])
def submit2():
    session.pop('guess')
    session.pop('secretnum')
    return redirect('/')
app.run(debug=True) # run our server
