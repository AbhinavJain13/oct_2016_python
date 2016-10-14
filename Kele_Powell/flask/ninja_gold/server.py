from flask import Flask, render_template, redirect, request, session
import datetime
import random
app=Flask (__name__)
app.secret_key="Orange"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']=0
    if 'activities' not in session:
        session['activities']=[]
    return render_template('index.html')
@app.route('/process_money', methods=["POST"])
def newgold():
    if request.form['building'] == "farm":
        session['building']="farm"
        session['num']=random.randint(10,20)
    elif request.form['building']=="cave":
        session['building']="cave"
        session['num']=random.randint(5,10)
    elif request.form['building']=="house":
        session['building']="house"
        session['num']=random.randint(2,5)
    elif request.form['building']=="casino":
        session['building']="casino"
        session['num']=random.randint(-50,50)
    session['gold']+=session['num']
    if request.form['building'] == "reset":
        session['gold']=0
    if session['num']>0:
        session['celebrate']="YAY!"
        session['class']='green'

    else:
        session['celebrate']="My wife is gunna kill me!"
        session['class']='red'
    data()
    return redirect('/')
def data():
    message_dict={
    'class':session['class'],
    'message':"You went to the {} and {} gold! {}" .format(session['building'], session['num'], session['celebrate'])}
    session['activities'].append(message_dict)

    if request.form['building'] == "reset":
        session.pop('activities')
    return redirect('/')


app.run(debug=True)
