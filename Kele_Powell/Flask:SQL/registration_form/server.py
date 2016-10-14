from flask import Flask, render_template, redirect,request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app=Flask(__name__)
app.secret_key="goldfish"

@app.route('/')
def index():
    if 'email' not in session:
        session['email']=""
    if 'first' not in session:
        session['first']=""
    if 'last' not in session:
        session['last']=""
    return render_template("index.html")



@app.route('/data',methods=['POST'])
def data():
    count=0
    session['email']=request.form['email']
    session['first']=request.form['first']
    session['last']=request.form['last']
    session['pass']=request.form['pass']
    session['repass']=request.form['repass']

    if len(request.form['email'])<1:
        flash(u"Please enter a valid email",'error')
        count=1
    if not EMAIL_REGEX.match(request.form['email']):
        flash(u"Need a valid Email",'error')
        count=1
    if len(request.form['first'])< 1:
        flash(u"Please enter a first name",'error')
        count=1
    if not request.form['first'].isalpha():
        flash(u"Please enter a first name without numbers or spaces",'error')
        count=1
    if len(request.form['last'])< 1:
        flash(u"Please enter a valid Last Name",'error')
        count=1
    if not request.form['last'].isalpha():
        flash(u"Please enter a last name without numbers",'error')
        count=1
    if len(request.form['pass'])< 1:
        flash(u"Please enter a password",'error')
        count=1
    if len(request.form['repass'])< 1:
        flash(u"Please confirm your password",'error')
        count=1
    if session['repass'] !=session['pass']:
        flash(u"Passwords Do not Match!",'error')
        count=1
    if count==1:
        return redirect('/')




    return redirect('/main')



@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/clear')
def clear():
        session.clear()
        return redirect('/')

app.run(debug=True)
