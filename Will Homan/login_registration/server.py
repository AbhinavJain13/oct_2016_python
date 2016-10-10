from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'usersdb')

@app.route('/')
def index():
    print(session['id'])
    return render_template('index.html')


@app.route('/register', methods=['Post'])
def process():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif len(request.form['first_name']) < 2:
          flash("First Name cannot be less than 2 charecters!")
    elif len(request.form['last_name']) < 2:
        flash("Last Name cannot be less than 2 charecters!")
    elif len(request.form['password']) < 1:
            flash("Password cannot be blank!")
    elif len(request.form['confirm_password']) < 1:
            flash("Confirm Password cannot be blank!")
    elif str.isalpha(request.form['first_name']) == False:
        flash("First Name cannot contain a number!")
    elif str.isalpha(request.form['last_name']) == False:
        flash("Last Name cannot contain a number!")
    elif len(request.form['password']) < 8:
        flash("Password cannot contain less than 8 charecters!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif request.form['confirm_password'] != request.form['password']:
        flash("Passwords do not match!")
    else:
        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password)
        query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'email': request.form['email'],
                 'pw_hash': pw_hash
               }
        mysql.query_db(query, data)
        user_query = "SELECT id FROM users WHERE email = :email"
        query_data = {
                        'email': request.form['email']
                    }
        id = mysql.query_db(user_query, query_data)
        session['id'] = id

        return redirect('/success')
    return redirect('/')

@app.route('/login', methods=['Post'])
def login():
    email = request.form['login_email']
    password = request.form['login_password']
    print(email)
    print(password)
    user_query = "SELECT * FROM users WHERE email = :email"
    query_data = {
                    'email': request.form['login_email']
                    }
    user = mysql.query_db(user_query, query_data)
    print('User is')
    print(user)
    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        user_query = "SELECT id FROM users WHERE email = :email"
        query_data = {
                        'email': request.form['login_email']
                    }
        id = mysql.query_db(user_query, query_data)
        session['id'] = id
        return redirect('/success')
    else:
        flash("Your login information was not correct.  Please try again")
        return redirect('/')

@app.route('/success')
def success():
    id = session['id']
    print('ID is')
    print(id[0]['id'])
    query = "SELECT * FROM users WHERE id = :id"
    data = {'id': id[0]['id']}
    users = mysql.query_db(query, data)
    return render_template('success.html', users = users)



app.run(debug=True)
