
from flask import Flask, request, redirect, render_template, session, flash
import md5
from flask_bcrypt import Bcrypt
# below: use the connection file's name without the extension!!
from mysqlconnection import MySQLConnector
# app it up
app = Flask(__name__)
# encryption
bcrypt = Bcrypt(app)
# specify the db
mysql = MySQLConnector(app,'friendsdb')

# Encryption test - can be removed if not needed
# password = 'password'
# encPw = md5.new(password).hexdigest()

password = 'password'
# encrypt the password we provided as 32 character string
encrypted_password = md5.new(password).hexdigest()
print 'encrypted: ',encrypted_password #this will show you the encrypted value
# 5f4dcc3b5aa765d61d8327deb882cf99 -> nice!

# Routes --------------------------------

# /
# Root (default)
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    # print "many friends ",friends
    # print friends
    return render_template('index.html',friends=friends)

# /friends
# Create a new friend
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends(first_name,last_name,occupation,created_at,updated_at) VALUES (:first_name,:last_name,:occupation,NOW(),NOW())"

     # run validations and if they are successful
     # we can create the password hash with bcrypt
    password = 'jeep'
    pw_hash = bcrypt.generate_password_hash(password)
    print 'PASSWORD hash: ',pw_hash

    data = {
        "first_name":       request.form['first_name'],
        "last_name":        request.form['last_name'],
        "occupation":       request.form['occupation']
        # ,"password":      pw_hash
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
