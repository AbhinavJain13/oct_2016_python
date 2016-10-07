
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print "many friends ",friends
    # print friends
    return render_template('index.html',all_friends=friends)
@app.route('/friends')
def create():
    print request.form['first_name']
    print request.form['last_name']
    print request.form['occupation']

@app.route('/friends/<friend_id>')
def show(friend_id):

    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    print "friend data: ", friend_id
    data = {'specific_id': friend_id}
    print "query data:",data
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', all_friends=friends)

app.run(debug=True)
