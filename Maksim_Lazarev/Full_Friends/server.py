import random
import re
from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnector(app,'full_friends')

@app.route('/')
def index():
    # print ("*** rendering index.html")
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', friends=friends)

@app.route("/friends", methods=['POST'])
def create():
    # print ("*** in process")
    if len(request.form['first_name']) < 1 or re.search('\d+', request.form['first_name']):
        flash("First name cannot be empty or contain any numbers!", 'error')
    if len(request.form['last_name']) < 1 or re.search('\d+', request.form['first_name']):
        flash("Last name cannot be empty or contain any numbers!", 'error')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'error')
    # if not CAP_REGEX.match(request.form['password']):
    #     flash("Password must contain ay least 1 uppercase letter and 1 numeric value", 'error')
    # if request.form['confirm_password'] != request.form['password']:
    #         flash("Confirm Password doesn't match the Password!", 'error')
    if "_flashes" not in session:
        query = "INSERT INTO friends (first_name, last_name, email) VALUES (:first_name, :last_name, :email)"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                'first_name':  request.form['first_name'],
                'last_name':  request.form['last_name'],
                 'email': request.form['email']
               }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        # flash("Success, you are now registered!", 'pass')
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    query="SELECT * FROM friends WHERE id=:id"
    data= {'id':id}
    friend = mysql.query_db(query, data)
    return render_template('friend_edit.html', friend=friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    data = {
            'id': id,
            'first_name':  request.form['first_name'],
            'last_name':  request.form['last_name'],
            'email': request.form['email']
            }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query="DELETE FROM friends WHERE id=:id"
    data= {'id':id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
