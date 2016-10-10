from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'walldb')

@app.route('/')
def index():
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
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'email': request.form['email'],
                 'password': pw_hash
               }
        mysql.query_db(query, data)
        user_query = "SELECT id FROM users WHERE email = :email"
        query_data = {
                        'email': request.form['email']
                    }
        id = mysql.query_db(user_query, query_data)
        session['id'] = id

        return redirect('/wall')
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
    if bcrypt.check_password_hash(user[0]['password'], password):
        user_query = "SELECT id FROM users WHERE email = :email"
        query_data = {
                        'email': request.form['login_email']
                    }
        id = mysql.query_db(user_query, query_data)
        session['id'] = id
        return redirect('/wall')
    else:
        flash("Your login information was not correct.  Please try again")
        return redirect('/')

@app.route('/logout', methods=['Post'])
def logout():
    session.clear()
    print(session)
    return render_template('logout.html')

@app.route('/submit_message', methods=['Post'])
def message():
    id = session['id']
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {
             'user_id': id[0]['id'],
             'message':  request.form['message_form']

           }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/wall')
def wall():
    id = session['id']
    query_messages = "SELECT users.first_name, users.last_name, messages.message, messages.created_at, messages.id FROM users LEFT JOIN messages ON users.id=user_id ORDER BY messages.created_at DESC"
    messages = mysql.query_db(query_messages)
    query_name = "SELECT users.first_name FROM users WHERE id = :id"
    data = {'id': id[0]['id'],}
    name = mysql.query_db(query_name, data)
    query_comments = "SELECT users.first_name, users.last_name, comments.comment, comments.created_at, comments.message_id FROM users LEFT JOIN messages ON users.id=messages.user_id LEFT JOIN comments ON messages.id=comments.message_id"
    comments = mysql.query_db(query_comments)
    return render_template('wall.html', messages = messages, name = name, comments=comments)

@app.route('/submit_comment/<message_id>', methods=['Post'])
def submit_comment(message_id):
    id = session['id']
    query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())"
    data = {
        'message_id': message_id,
        'user_id': id[0]['id'],
        'comment': request.form['comment_form']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)
