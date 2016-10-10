from flask import Flask, render_template, request, redirect, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="MEOWmeowMEOW"

# import the Connector function
from mysqlconnection import MySQLConnector

# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friends')
# an example of running a query

@app.route('/', methods=['GET'])
def index():
    query = 'SELECT * FROM friends'
    friends = mysql.query_db(query)
    return render_template("index.html", friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = 'INSERT INTO friends(first,last,email,created_at,updated_at) VALUES(:first,:last,:email,now(),now())'
    data = {
        'first': request.form["first"],
        'last': request.form["last"],
        'email': request.form["email"]
    }
    mysql.query_db(query, data)
    return redirect("/")

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
    query = 'SELECT * FROM friends WHERE id=:id'
    data = {
        'id':id
    }
    friend = mysql.query_db(query, data)
    return render_template("friends.html", friend=friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = 'UPDATE friends SET first=:first,last=:last,email=:email,updated_at=NOW() WHERE id=:id'
    data = {
        'id':id,
        'first': request.form["first"],
        'last': request.form["last"],
        'email': request.form["email"]
    }
    mysql.query_db(query, data)
    return redirect("/")

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
    query = 'DELETE FROM friends WHERE id=:id'
    data = {
        'id':id
    }
    mysql.query_db(query, data)
    return redirect("/")
app.run(debug=True)
