
from flask import Flask, request, redirect, render_template, session, flash
import md5
import re
from flask_bcrypt import Bcrypt
# below: use the connection file's name without the extension!!
from mysqlconnection import MySQLConnector
# app it up
app = Flask(__name__)
# encryption
bcrypt = Bcrypt(app)
# specify the db
mysql = MySQLConnector(app,'friendsdb')

app.secret_key = 'someKey'

# Functions -----------------------------------------

def validate_email(email):
    return re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

def validate_letters_2(string):
    return re.match('[a-zA-Z]{2}',string)

def validate_chars_8(string):
    return re.match('/w{8}',string)

# Routes --------------------------------------------

# /
# Root (default)
@app.route('/',methods=['GET'])
def index():
    try:
        "InDEX!! ",session['current_user']

        return render_template('index.html')

        #
        # logged_in_id = SESSION['current_user']
        # # For a logged in user, we're going to look up ad display their friends
        # data={
        #     "logged": logged_in_id
        #     }
        # friends = mysql.query_db("SELECT * FROM friends WHERE id= :logged_in_id",data)
        # # print "many friends ",friends
        # return render_template('index.html',friends=friends)

    except:
        print "not logged in"
        return redirect('/login')

# LOGIN -----------------------------------------------

@app.route('/login',methods=['POST','GET'])
def login():
    try:
        # validation

# First Name - letters only, at least 2 characters and that it was submitted
# Last Name - letters only, at least 2 characters and that it was submitted
# Email - Valid Email format, and that it was submitted
# Password - at least 8 characters, and that it was submitted
# Password Confirmation - matches password

        # if len(request.form['email']) < 1:
        #     flash("Email cannot be empty!") # just pass a string to the flash function
        # else:
        #     flash("Success! Your email is {}".format(request.form['email']))


        email= request.form['email']
        query =  '''SELECT * FROM users WHERE email= :email LIMIT 1'''
        data = {
            email: email
            }
        attempt_user = mysql.query_db(query,data)
        if bcrypt.check_password_hash(attempt_user[0]['pw_hash'], password):
            session['current_user'] = attempt_user[0]
            return redirect('/')
        else:
            return redirect('/login')
    except:


        return render_template('login.html')



# REGISTRATION ________________________________________
@app.route('/registration',methods=['POST','GET'])
def register():

    try: #to validate and register
        # print 'REGISTRATION POST: ',request.form
        first_name =        request.form['first_name']
        last_name =         request.form['last_name']
        email =             request.form['email']
        password =          request.form['password']
        password_confirm =  request.form['password_confirm']

        # VALIDATE FORM data


        # IF VALID...

        # Encrypt password
        pw_hash = bcrypt.generate_password_hash(password)
        print 'PASSWORD hash: ',pw_hash

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

        print 'NEW USER ID: ',new_user_id

        # GRAB THE COMPLETE USER now....
        query_full = '''SELECT * FROM users WHERE id = :id'''
        data_full = {
            "id":   new_user_id
            }
        current_user = mysql.query_db(query_full,data_full)
        # session['current_user'] = current_user
        # print 'And, the current user: ',current_user[0]
        session['current_user'] = current_user[0]
        print 'Made it!! ',session['current_user']
        return redirect('/')

    except:
        #raise
        return render_template('registration.html')




# FRIENDS ROUTES --------------------------------------

# /friends
# Create a new friend
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends(first_name,last_name,occupation,created_at,updated_at) VALUES (:first_name,:last_name,:occupation,NOW(),NOW())"

     # run validations and if they are successful
     # we can create the password hash with bcrypt

    data = {
        "first_name":       request.form['first_name'],
        "last_name":        request.form['last_name'],
        "occupation":       request.form['occupation']
        }
    mysql.query_db(query,data)
    return redirect('/')

# /friends/<id>
# Show a single friend by id
@app.route('/friends/<id>',methods=['POST','GET'])
def show(id):
    # POST it is an update
    if request.method == "POST":
        query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
        data = {
                 'first_name':  request.form['first_name'],
                 'last_name':   request.form['last_name'],
                 'occupation':  request.form['occupation'],
                 'id':          request.form['id']
               }
        mysql.query_db(query, data)
        return redirect('/')

    # GET it is a show a single friend
    else:
        query = "SELECT * FROM friends WHERE id = :id"
        data = {'id': id}
        friends = mysql.query_db(query, data)
        return render_template('index.html', friends=friends)

# Update a friend by id
# /friends/<id>/edit
@app.route('/friends/<id>/edit', methods=['POST','GET'])
def update(id):
    # POST it is an update
    if request.method == "POST":
        friend={
            'first_name':  request.form['first_name'],
            'last_name':   request.form['last_name'],
            'occupation':  request.form['occupation'],
            'id':          request.form['id']
        }
        print 'posted friend: ',friend
        return render_template('edit.html', friend=friend)
    # GET the information and ready the page for editing
    else:
        query = "SELECT * FROM friends WHERE id = :id"
        data = {'id': id}
        print "query data:",data
        friend = mysql.query_db(query, data)
        print 'returned friend: ',friend
        return render_template('edit.html', friend=friend[0])

# /friends/<id>/delete
# Delete a friend by id
@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
