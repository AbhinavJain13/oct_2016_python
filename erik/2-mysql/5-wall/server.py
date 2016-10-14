
from flask import Flask, request, redirect, render_template, session, flash
import md5
import re
from flask_bcrypt import Bcrypt
# below: use the connection file's name without the extension!!
from mysqlconnection import MySQLConnector
# app it up
app = Flask(__name__)
app.secret_key = 'OnlyInAJeep'
# encryption
bcrypt = Bcrypt(app)
# specify the db
mysql = MySQLConnector(app,'wall')


# Functions -----------------------------------------

def validate_email(email):
    return re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

def validate_letters_2(string):
    return re.match('[a-zA-Z]{2,}',string)

def validate_chars_8(string):
    return re.match('\w{8,}',string)

def passwords_match(pw1,pw2):
    return pw1==pw2

def check_logged_in():
    if session.has_key('current_user'):
        #print "User is logged in."
        return True
    else:
        return False


# Routes --------------------------------------------

# /
# Root (default)
@app.route('/',methods=['GET'])
def index():
    try:
        current_user_id = session['current_user']['id']
        session['show_login'] = 0

        # GET MESSAGES & COMMENTS
        query =  '''SELECT m.id msgid, m.user_id muserid, m.body mbody, m.updated_at mdate, c.id cmtid, c.body cbody
                    FROM messages m
                    LEFT JOIN comments c ON m.id = c.message_id
                    ORDER BY msgid,cmtid DESC
                 '''
        all_messages = mysql.query_db(query)
        print 'got back this messages: ',all_messages
        return render_template('index.html',messages=all_messages)

    except:
        print "Not logged in"
        session['show_login'] = 1
        return render_template('index.html')

# LOGIN / LOGOUT -----------------------------------------------

# /login
# Login a user
@app.route('/login',methods=['POST','GET'])
def login():
    if check_logged_in():
        return redirect('/')
    try:
        # validation
        email = request.form['email']
        password = request.form['password']
        if(not validate_email(email)):
            flash("Email is not valid!",category='email')
            return redirect('/')

        query =  '''SELECT * FROM users WHERE email= :email LIMIT 1'''
        data = {
            "email": email
            }
        attempt_user = mysql.query_db(query,data)
        # print "ATTEMPTED USER: ",attempt_user[0]
        # print "ATTEMPTED USER PASS: ",attempt_user[0]['password']
        if bcrypt.check_password_hash(attempt_user[0]['password'], password):
            session['current_user'] = attempt_user[0]
            session['show_login'] = 0
            return redirect('/')
        else:
            flash("Password is not valid!",category='password')
            return redirect('/')
    except:
        raise
        return render_template('index.html')

# /logout
# Log out the user
@app.route('/logout',methods=['GET'])
def logout():
    session.clear()
    return redirect('/')

# REGISTRATION ________________________________________

# /registration
# Create a new user
@app.route('/registration',methods=['POST','GET'])
def register():
    if check_logged_in():
         return redirect('/')
    try:
        first_name =        request.form['first_name']
        last_name =         request.form['last_name']
        email =             request.form['email']
        password =          request.form['password']
        password_confirm =  request.form['password_confirm']

        # VALIDATE FORM data
        errors_flag = False
        if(not validate_letters_2(first_name)):
            flash('First Name invalid!',category='rfirst')
            errors_flag = True
        if(not validate_letters_2(last_name)):
            flash('First Name invalid!',category='rlast')
            errors_flag = True
        if(not validate_email(email)):
            flash('Invalid email address!',category='remail')
            errors_flag = True
        if(not validate_chars_8(password) or not validate_chars_8(password_confirm)):
            flash('Password not long enough!',category='rpassword')
            errors_flag = True
        if(not passwords_match(password,password_confirm)):
            flash('Passswords do not match!',category='rpassword')
            errors_flag = True
        print "ERRORS FLAG: ",errors_flag

        if(errors_flag):
            return redirect ('/')

        pw_hash = bcrypt.generate_password_hash(password)

        data = {
            "first_name":   first_name,
            "last_name" :   last_name,
            "email":        email,
            "password":     pw_hash
        }

        query = '''INSERT INTO users(first_name,last_name,email,password,created_at,updated_at)
                   VALUES (:first_name,:last_name,:email,:password,NOW(),NOW())'''
        # the new user's id is returned by the INSERT
        new_user_id = mysql.query_db(query,data)

        # GRAB THE COMPLETE USER now....
        query_full = '''SELECT * FROM users WHERE id = :id'''
        data_full = {
            "id":   new_user_id
        }
        current_user = mysql.query_db(query_full,data_full)

        session['current_user'] = current_user[0]
        session['show_login'] = 0
        #flash("Success! Created user {{}}.format(session['current_user']['first_name'])",category='success')
        return redirect('/')

    except:
        #raise
        return redirect('/')


# MESSAGES ROUTES --------------------------------------

# /messages
# Create a new message
@app.route('/messages', methods=['POST'])
def create():

    # run validations and if they are successful...

    query = "INSERT INTO messages(user_id,body,created_at,updated_at) VALUES (:user_id,:body,NOW(),NOW())"

    data = {
        "user_id":       session['current_user']['id'],
        "body":          request.form['message']
        }
    mysql.query_db(query,data)
    session['show_login'] = 0
    return redirect('/')

# /comments
# Create a new comment
@app.route('/comments', methods=['POST'])
def createcomment():

    # run validations and if they are successful...

    query = "INSERT INTO comments(user_id,message_id,body,created_at,updated_at) VALUES (:user_id,:message_id,:body,NOW(),NOW())"

    data = {
        "user_id":          request.form['muserid'],
        "message_id":       request.form['msgid'],
        "body":             request.form['comment']
        }
    mysql.query_db(query,data)
    session['show_login'] = 0
    return redirect('/')

app.run(debug=True)
