from flask import Flask, render_template, request, redirect, session, flash
# imports the Bcrypt module
from flask_bcrypt import Bcrypt
# imports regex
import re

#regex
NAME_REGEX = re.compile(r'^[a-zA-Z-]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key="MEOWmeowMEOW"

# import the Connector function
from mysqlconnection import MySQLConnector

# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'login')
# an example of running a query

@app.route('/', methods=['GET'])
def index():
    if "email" not in session:
        return render_template("index.html")
    if "match" not in session:
        session["match"] == 0
    else:
        return render_template("success.html")

@app.route('/login', methods=['POST'])
def login():
    login_query = "SELECT hash FROM login where email=:email"
    login_data = {
        'email':request.form['email'],
    }

    hashpass = mysql.query_db(login_query, login_data)
    password = request.form['password']

    ####nonexistant entry will bcrypt to fail
    if not hashpass:
        session["match"] = 1
        return redirect("/")
    elif(bcrypt.check_password_hash(hashpass[0]['hash'], password)):
        session["email"]=login_data["email"]
        return render_template("success.html")
    ###password exists but does not match
    else:
        session["match"] = 1
        return redirect("/")

@app.route('/register', methods=['POST'])
def create():
    insert_query = "INSERT INTO login(first, last, email, hash, created_at, updated_at) VALUES (:first, :last, :email, :hash, NOW(), NOW())"
    password = request.form['password']
    confirm = request.form['confirm']

    #run test loops, if successful store capitalized first and last names and encyrpted password
    check = {
        'passwordlen':[0, "Password minimum length of 8 required."],
        'passwordmatch':[0, "Passwords do not match."],
        'nameslen':[0, "First and last name minimum length of 2 required."],
        'namesregex':[0, "First and Last names must contain only alphabetical characters."],
        'emailregex':[0, "Invalid e-mail."],

    }

    if not password or not (password > 7):
        check['passwordlen'][0] = 1
    if not (password == confirm):
        check['passwordmatch'][0] = 1
    if not (len(request.form['first']) > 2 or len(request.form['last']) > 2):
        check['nameslen'][0] = 1
    if not NAME_REGEX.match(request.form["first"]) or not NAME_REGEX.match(request.form["last"]):
        check['namesregex'][0] = 1
    if not (EMAIL_REGEX.match(request.form["email"])):
        check['emailregex'][0] = 1

    if check['passwordlen'][0] == 1 or check['passwordmatch'][0] == 1 or check['nameslen'][0] == 1 or check['namesregex'][0] == 1 or check['emailregex'][0] == 1:
        ###if login attempt was made and unssuccessful, clear login fail then create message sessions
        session.clear()
        for i in check:
            if check[i][0] == 1:
                flash(check[i][1])
        return redirect("/")
    else:
        insert_data = {
            'first': request.form['first'].capitalize(),
            'last': request.form['last'].capitalize(),
            'email': request.form['email'],
            'hash': bcrypt.generate_password_hash(password)
        }

        mysql.query_db(insert_query, insert_data)
        session["email"]=insert_data["email"]
        return render_template("success.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
