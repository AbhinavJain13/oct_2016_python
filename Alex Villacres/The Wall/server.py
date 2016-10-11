from flask import Flask, render_template, redirect, flash, request, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "Shhhhhhhhhhhhhhhhhhhhhhhhhhh"

mysql = MySQLConnector(app, 'wall')
bcrypt = Bcrypt(app)

# email regex here
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # check for errors
    message = False
    if len(request.form['first_name']) < 2:
        flash('First name 2 short!')
        message = True
    if len(request.form['last_name']) < 2:
        flash('Last name 2 short!')
        message = True
    if not email_regex.match(request.form['email']):
        flash('Email not valid!')
        message = True
    if len(request.form['password']) < 8:
        flash('Password must be at least 8 characters.')
        message = True
    if request.form['confirm'] != request.form['password']:
        flash('Passwords do not match!')
        message = True
    if message == True:
        return redirect('/')
    else:
        hashpass = bcrypt.generate_password_hash(request.form['password'])
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashpass
        }
        new_user = mysql.query_db(query, data)
        session['user_id'] = new_user
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        return redirect('/wall')
    # if false, flash error, then redirect index
    # if true, add to database and redirect to wall
    #          add user to session

@app.route('/login', methods=['POST'])
def login():
    # check for errors, flash error if false
    query = 'SELECT * FROM users WHERE email = :email'
    data = {
        'email': request.form['email']
    }
    user = mysql.query_db(query, data)
    if not user:
        flash('user not found')
        return redirect('/')
    elif not bcrypt.check_password_hash(user[0]['password'], request.form['password']):
        flash('invalid')
        return redirect('/')
    else:
        session['user_id'] = user[0]['id']
        session['first_name'] = user[0]['first_name']
        session['last_name'] = user[0]['last_name']
        return redirect('/wall')

@app.route('/wall')
def showAll():
    # SELECT * FROM wall.messages;
    query = 'SELECT * FROM wall.messages JOIN users ON users.id = messages.user_id'
    messages = mysql.query_db(query)
    # show messages - return render_template('wall.html', messages=messages)

    # THATS IT! KICKASS!
    return render_template('wall.html', messages = messages)

@app.route('/message', methods=['POST'])
def message():
    # grab data from form, insert to database
    if not request.form['message']:
        flash('you entered nothing')
        return redirect('/wall')
    # redirect to the wall
    query = 'INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :user_id)'
    data = {
        'message': request.form['message'],
        'user_id': session['user_id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)
