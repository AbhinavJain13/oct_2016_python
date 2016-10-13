import random
import re
import datetime
import time
from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# CAP_REGEX = re.compile(r'^(?=.*[0-9]+.*)(?=.*[A-Z]+.*)[a-zA-Z0-9.+_-]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'secret'
mysql = MySQLConnector(app,'wall')

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
        if (bcrypt.check_password_hash(user[0]['password'], request.form['password'])):
        # if (password==user[0]['password']):
            session['user_id']=user[0]['id']
            return redirect('/wall')
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
            password = bcrypt.generate_password_hash(request.form['password'])
            query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"
            # We'll then create a dictionary of data from the POST data received.
            data = {
                    'first_name':  request.form['first_name'],
                    'last_name':  request.form['last_name'],
                    'email': request.form['email'],
                    'password': password
                    }
            # Run query, with dictionary values injected into the query.
            session['user_id']=mysql.query_db(query, data)
            # print (user_id)
            # flash("profile, you are now registered!", 'pass')
            return redirect('/wall')
    else:
        return redirect('/')

@app.route('/wall')
def wall():
    query="SELECT first_name FROM users WHERE id=:id"
    data= {'id': session['user_id']}
    user = mysql.query_db(query, data)
    query="SELECT messages.*, CONCAT(first_name,' ',last_name) AS name FROM messages LEFT JOIN users on messages.user_id = users.id ORDER BY messages.created_at DESC"
    messages = mysql.query_db(query, data)
    # print (messages)
    msg_comments=[]
    for message in messages:
        # print (message)
        print (message['name'])
        query="SELECT comments.*, CONCAT(first_name,' ',last_name) AS name FROM comments LEFT JOIN users on comments.user_id = users.id WHERE comments.message_id=:msg_id ORDER BY comments.created_at ASC"
        data= {'msg_id': message['id']}
        comments = mysql.query_db(query, data)
        # print (comments)
        msg_comments.append([message, comments])
        # return render_template('wall.html', user=user, messages=messages)
    # print (msg_comments[0])
    return render_template('wall.html', user=user, msg_comments=msg_comments)


@app.route('/user/profile')
def profile():
    query="SELECT * FROM users WHERE id=:id"
    data= {'id': session['user_id']}
    user = mysql.query_db(query, data)
    return render_template('profile.html', user=user)

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
            password = bcrypt.generate_password_hash(request.form['password'])
            query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, password= :password WHERE id = :id"
            data = {
                    'id': session['user_id'],
                    'first_name':  request.form['first_name'],
                    'last_name':  request.form['last_name'],
                    'email': request.form['email'],
                    'password': password
                    }
            mysql.query_db(query, data)
            return redirect('/user/profile')
    else:
        return redirect('/user/edit')

@app.route('/user/delete', methods=['POST'])
def destroy():
    query="DELETE FROM users WHERE id=:id"
    data= {'id': session['user_id']}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/message/post', methods=['POST'])
def message_post():
    query = "INSERT INTO messages (user_id, message) VALUES (:user_id, :message)"
    data = {
            'user_id':  session['user_id'],
            'message': request.form['txtMsg']
            }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comment/post', methods=['POST'])
def comment_post():
    query = "INSERT INTO comments (user_id, message_id, comment) VALUES (:user_id, :message_id, :comment)"
    data = {
            'user_id':  session['user_id'],
            'message_id': request.form['msg_id'],
            'comment': request.form['txtCmt']
            }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/message/delete', methods=['POST'])
def message_delete():
    query="DELETE FROM comments WHERE message_id=:message_id"
    data= {'message_id': request.form['msg_id']}
    mysql.query_db(query, data)
    query="DELETE FROM messages WHERE id=:message_id"
    data= {'message_id': request.form['msg_id']}
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)
