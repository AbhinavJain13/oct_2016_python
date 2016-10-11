from flask import Flask, render_template, request, redirect, session, flash
# imports the Bcrypt module
from flask_bcrypt import Bcrypt
# import the Connector function
from mysqlconnection import MySQLConnector
# imports regex
import re

#regex
NAME_REGEX = re.compile(r'^[a-zA-Z-]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key="MEOWmeowMEOW"

# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'liansu')
# an example of running a query

@app.route('/', methods=['GET'])
def index():
    ###first visit, user session DNE
    if "user" not in session:
        return render_template("index.html")
    ###user already logged in, redirect to wall
    else:
        return redirect("/wall")

@app.route('/login', methods=['POST'])
def login():
    ###take entered email and request db for hash
    login_query = 'SELECT hash FROM users where email=:email'
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
        #store id/first/last/email to session
        user_query = 'SELECT id,first,last,email FROM users where email=:email'
        session["user"] = mysql.query_db(user_query,login_data)
        return redirect("/wall")
    ###password exists but does not match
    else:
        session["match"] = 1
        return redirect("/")

@app.route('/register', methods=['POST'])
def create():
    insert_query = 'INSERT INTO users(first, last, email, hash, created_at, updated_at) VALUES (:first, :last, :email, :hash, NOW(), NOW())'
    password = request.form['password']
    confirm = request.form['confirm']

    #run test loops against request entries, if successful then store into DB capitalized first and last names and encyrpted password
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
        #store id/first/last/email to session
        user_query = 'SELECT id,first,last,email FROM users where email=:email'
        session["user"] = mysql.query_db(user_query,request.form['email'])
        return redirect("/wall")

@app.route('/wall')
def wall():
    #Block users from seeing main.html template by redirecting them to /
    if "user" not in session:
        return redirect("/")
    else:
        ###query all messages, session["message_query"][<index>]["id"] to find post
        session["message_query"] = mysql.query_db('SELECT messages.id,first,last,message,messages.updated_at FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.updated_at DESC')
        session["comment_query"] = mysql.query_db('SELECT comments.message_id,first,last,comment,comments.updated_at FROM messages JOIN comments ON messages.id = comments.message_id JOIN users ON users.id = comments.user_id ORDER BY comments.updated_at DESC')
        print session["comment_query"]
        return render_template("main.html")

@app.route('/postmessage/', methods=["POST"])
def postmessage():
    postmessage_query = 'INSERT INTO messages(user_id,message,created_at,updated_at) VALUES (:user_id, :message, NOW(), NOW())'
    postmessage_data = {
        'user_id':session["user"][0]["id"],
        'message':request.form['message']
    }
    mysql.query_db(postmessage_query, postmessage_data)
    return redirect("/wall")

@app.route('/postcomment/<id>', methods=["POST"])
def postcomment(id):
    postcomment_query = 'INSERT INTO comments(user_id,message_id,comment,created_at,updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())'
    postcomment_data = {
        'user_id':session["user"][0]["id"],
        'message_id': id ,
        'comment':request.form['comment']
    }
    mysql.query_db(postcomment_query, postcomment_data)
    return redirect("/wall")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
