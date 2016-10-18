from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route("/")
def number():
    if 'secret' not in session:
        session['secret']= random.randrange(0,101)
    print(session['secret'])
    return render_template('index.html')
@app.route('/guess', methods = ['POST'])
def guess():
    if request.form['number']:
        session['guess']=int(request.form['number'])
    return redirect('/')
@app.route('/reset')
def back():
    del session['guess']
    del session['secret']
    return redirect('/')
app.run(debug=True)
