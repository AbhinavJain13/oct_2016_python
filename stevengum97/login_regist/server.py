from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key='OogaBooga'
EREG = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
PWREG = re.compile('.*\s')

mysql = MySQLConnector(app, 'login_r')
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    if 'user' in session:                       ## checks session to see if a user is in play, session['user'] is generated through line 43
        return redirect('/success')
    return render_template('index.html')

@app.route('/new_user', methods=['post'])
def new_user():
    user = request.form                         ## 'user = request.form'; generic form submission of information
    errors = validate("new_user", user)

    if not errors:
        password = bcrypt.generate_password_hash(user['password'])
        query = """INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
        VALUES (:first_name, :last_name,:email, :password, NOW(), NOW())"""
    #
        data = {
        'first_name': user['first_name'],
        'last_name': user['last_name'],
        'email': user['email'],
        'password': password,
        }
        mysql.query_db(query, data)
    #
        data = {'email': user['email']} ## reference to 'user = request.form'; generic form submission of information
                                        ## the contents of 'user = request.form' depends on the route of submission
        query = """SELECT * FROM users WHERE email=:email"""
    #
        session['user'] = mysql.query_db(query, data)[0]   ## stores the user as the session user. queries db and returns first value as session['user']
                                                        ## wouldn't this target the p-key, 'id'?
        return redirect('/success')
    else:
        generate_flashes(errors)
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    user = request.form
    errors = validate("login", user)
    if not errors:
        query = """SELECT * FROM users WHERE email=:email"""
        data = {'email' : user['email']}
        session['user'] = mysql.query_db(query, data)[0]
        return redirect('/success')
    else:
        generate_flashes(errors)
        return redirect('/')

@app.route('/success')
def wall():
    return render_template('success.html', user = session['user'])  ## renders success.html with the session's user stored

@app.route('/logout')
def logout():
    session.pop('user', None)       ## clears session['user'] as part of the logout process
    return redirect('/')

def validate(type, input):
    errors = []
    if type == "new_user":
        first_name = input['first_name']
        last_name = input['last_name']
        email = input['email']
        password = input['password']
        if not first_name:
            errors.append(("Please enter your first name!","fname_error"))
        elif len(first_name) < 2 or not first_name.isalpha():
            errors.append(("First name is invalid!","fname_error"))
        if not last_name:
            errors.append(("Please enter your last name!","lname_error"))
        elif len(last_name) < 2 or not last_name.isalpha():
            errors.append(("Last name is invalid!","lname_error"))
        if not email:
            errors.append(("Please enter your email!","email_error"))
        elif not EREG.match(email):
            errors.append(("Email is invalid!","email_error"))
        if not password:
            errors.append(("Please create a new password.","pw_error"))
        elif PWREG.match(password) or len(password) < 8:
            errors.append(("Password must meet requirements.","pw_error"))
        if not password == input['confirm_pw']:
            errors.append(("The passwords entered don't match.","confirm_error"))

        query = """SELECT * FROM users WHERE email=:email"""
        data = {'email' : email}
        user = mysql.query_db(query, data)
        if user:
            errors.append(("Email address already exists!","reg_error"))

    elif type == "login":
        user = mysql.query_db("""SELECT * FROM users WHERE email=:email""", {'email' : input['email']})
        if user:
            if not bcrypt.check_password_hash(user[0]['password'], input['password']):
                errors.append(("Incorrect password!","login_pw_error"))
        else:
            errors.append(("Email address doesn't exist!","login_user_error"))
    return errors

def generate_flashes(error_list):
    for error in error_list:
        flash(error[0], error[1])



if __name__ == '__main__':
    app.run(debug=True)
