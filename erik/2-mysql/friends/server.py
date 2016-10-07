
from flask import Flask, request, redirect, render_template, session, flash
# below: use the connection file's name without the extension!!
from mysqlconnection import MySQLConnector
# app it up
app = Flask(__name__)
# specify the db....
mysql = MySQLConnector(app,'friendsdb')

# Routes --------------------------------

# /
# Root (default)
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print "many friends ",friends
    # print friends
    return render_template('index.html',all_friends=friends)

# /friends
# Create a new friend
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends(first_name,last_name,occupation,created_at,updated_at) VALUES (:first_name,:last_name,:occupation,NOW(),NOW())"
    data = {
        "first_name":    request.form['first_name'],
        "last_name":     request.form['last_name'],
        "occupation":    request.form['occupation'],
        "created_at":    request.form['created_at'],
        "updated_at":    request.form['updated_at']
        }
    mysql.query_db(query,data)
    return redirect('/')

# /friends/<friend_id>
# Show a single friend by id
@app.route('/friends/<friend_id>')
def show(friend_id):
    # to insert param variable :variable_name
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    print "friend data: ", friend_id
    data = {'specific_id': friend_id}
    print "query data:",data
    # Execute query, passing in a parameter obj
    friends = mysql.query_db(query, data)
    # pass expected parameter(s) to the page to be rendered
    return render_template('index.html', all_friends=friends)

# /update_friend/<friend_id>
# Update a friend by id
@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')

# /unfriend/<friend_id>
# Remove a friend by id
@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
