import random
import re
from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# CAP_REGEX = re.compile(r'^(?=.*[0-9]+.*)(?=.*[A-Z]+.*)[a-zA-Z0-9.+_-]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'secret'
mysql = MySQLConnector(app,'login_registration')

@app.route('/')
def index():
    # print ("*** rendering index.html")
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def login():
    query="SELECT * FROM users WHERE email=:email"
    data= {
            'email': request.form['email'],
          }
    user=mysql.query_db(query, data)
    if (user):
        if (bcrypt.check_password_hash(user[0]['pw_hash'], request.form['password'])):
        # if (pw_hash==user[0]['pw_hash']):
            session['user_id']=user[0]['id']
            return redirect('/success')
        else:
            flash("Password is incorrect!", 'error')
    else:
        flash("No user with such email registered. Please check email or register first!", 'error')
    return redirect('/')

@app.route("/register", methods=['POST'])
def create():
    # print ("*** in process")
    if len(request.form['first_name']) < 2 or re.search('\d+', request.form['first_name']):
        flash("First name must be at least 2 characters long and can't contain any numbers!", 'error')
    if len(request.form['last_name']) < 2 or re.search('\d+', request.form['first_name']):
        flash("Last name must be at least 2 characters long and can't contain any numbers!", 'error')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'error')
    # if not CAP_REGEX.match(request.form['password']):
    #     flash("Password must contain ay least 1 uppercase letter and 1 numeric value", 'error')
    if len(request.form['password']) < 8:
         flash("Password must be at least 8 characters long", 'error')
    if request.form['confirm_password'] != request.form['password']:
        flash("Confirm Password doesn't match the Password!", 'error')
    if "_flashes" not in session:
        query="SELECT * FROM users WHERE email=:email"
        data= {
                'email': request.form['email'],
              }
        user=mysql.query_db(query, data)
        if (user):
            flash("User with such email already registered! Please login or chose another email.", 'error')
            return redirect('/')
        else:
            pw_hash = bcrypt.generate_password_hash(request.form['password'])
            query = "INSERT INTO users (first_name, last_name, email, pw_hash) VALUES (:first_name, :last_name, :email, :pw_hash)"
            # We'll then create a dictionary of data from the POST data received.
            data = {
                    'first_name':  request.form['first_name'],
                    'last_name':  request.form['last_name'],
                    'email': request.form['email'],
                    'pw_hash': pw_hash
                    }
            # Run query, with dictionary values injected into the query.
            session['user_id']=mysql.query_db(query, data)
            # print (user_id)
            # flash("Success, you are now registered!", 'pass')
            return redirect('/success')
    else:
        return redirect('/')

@app.route('/success')
def succes():
        query="SELECT * FROM users WHERE id=:id"
        data= {'id': session['user_id']}
        user = mysql.query_db(query, data)
        return render_template('success.html', user=user)

@app.route('/user/edit')
def edit():
    query="SELECT * FROM users WHERE id=:id"
    data= {'id': session['user_id']}
    user = mysql.query_db(query, data)
    return render_template('user_edit.html', user=user)

@app.route('/user/update', methods=['POST'])
def update():
    if len(request.form['first_name']) < 2 or re.search('\d+', request.form['first_name']):
        flash("First name must be at least 2 characters long and can't contain any numbers!", 'error')
    if len(request.form['last_name']) < 2 or re.search('\d+', request.form['first_name']):
        flash("Last name must be at least 2 characters long and can't contain any numbers!", 'error')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'error')
    # if not CAP_REGEX.match(request.form['password']):
    #     flash("Password must contain ay least 1 uppercase letter and 1 numeric value", 'error')
    if len(request.form['password']) < 8:
         flash("Password must be at least 8 characters long", 'error')
    if request.form['confirm_password'] != request.form['password']:
        flash("Confirm Password doesn't match the Password!", 'error')
    if "_flashes" not in session:
        query="SELECT * FROM users WHERE email=:email AND id!=:id"
        data= {
                'email': request.form['email'],
                'id': session['user_id']
              }
        user=mysql.query_db(query, data)
        if (user):
            flash("That email nas been already used! Please chose another email.", 'error')
            return redirect('/user/edit')
        else:
            pw_hash = bcrypt.generate_password_hash(request.form['password'])
            query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, pw_hash= :pw_hash WHERE id = :id"
            data = {
                    'id': session['user_id'],
                    'first_name':  request.form['first_name'],
                    'last_name':  request.form['last_name'],
                    'email': request.form['email'],
                    'pw_hash': pw_hash
                    }
            mysql.query_db(query, data)
            return redirect('/success')
    else:
        return redirect('/user/edit')

@app.route('/user/delete', methods=['POST'])
def destroy():
    query="DELETE FROM users WHERE id=:id"
    data= {'id': session['user_id']}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
