from flask import Flask, render_template, redirect,request, session, flash
import re
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app=Flask(__name__)
app.secret_key="goldfish"
bcrypt= Bcrypt(app)
mysql=MySQLConnector(app,'login_register')

@app.route('/')
def index():
    if 'email' not in session:
        session['email']=""
    if 'first' not in session:
        session['first']=""
    if 'last' not in session:
        session['last']=""
    query= "select* from users order by created_at DESC"
    friends=mysql.query_db(query)
    return render_template("index.html",friends=friends)




@app.route('/register',methods=['POST'])
def register():
    count=0
    session['email']=request.form['email']
    session['first']=request.form['first']
    session['last']=request.form['last']

    email_check= "SELECT email from users"
    emails=mysql.query_db(email_check)
    for emaily in emails:
        if emaily['email']==request.form['email']:
            flash(u"email already taken",'error')
            count=1

    if len(request.form['email'])<3:
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
    if len(request.form['pass'])< 7:
        flash(u"Please enter a password",'error')
        count=1
    if len(request.form['repass'])< 7:
        flash(u"Please confirm your password",'error')
        count=1
    if request.form['repass'] !=request.form['pass']:
        flash(u"Passwords Do not Match!",'error')
        count=1
    if count==1:
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pass'])

    query= "INSERT INTO users (email, first_name, last_name, password, created_at, updated_at) VALUES (:email, :first_name, :last_name, :password, NOW(), NOW())"
    data={
    "email":session['email'],
    "first_name":session['first'],
    "last_name":session['last'],
    "password":pw_hash,
    }
    mysql.query_db(query,data)
    flash(u"successfully registered!",'success')
    return redirect('/success')

@app.route('/login',methods=['POST'])
def login():
    count=0
    session['email']=request.form['email']
    if len(request.form['email'])<3:
        flash(u"Email too short",'error')
        count=1
    if not EMAIL_REGEX.match(request.form['email']):
        flash(u"Need a valid Email",'error')
        count=1
    if len(request.form['pass'])< 7:
        flash(u"Please enter a password",'error')
        count=1
    if count==1:
        return redirect('/')
    query="Select * from users where email=:email LIMIT 1"
    data={
    "email":request.form['email']
    }

    user=mysql.query_db(query,data)
    if bcrypt.check_password_hash(user[0]['password'],request.form['pass']):
        flash(u"successfully logged in!",'success')
        return redirect('/success')
    else:
        flash(u"Email and password do not match. please try again",'error')
        return redirect('/')



@app.route('/success')
def main():
    return render_template('success.html')

@app.route('/logout')
def logout():
        session.clear()
        flash(u'succesfully logged out!',"success")
        return redirect('/')

app.run(debug=True)
