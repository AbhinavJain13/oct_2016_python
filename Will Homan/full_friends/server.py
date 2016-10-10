from flask import Flask, request, redirect, render_template, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
        query = "SELECT * FROM friends"
        friends = mysql.query_db(query)
        return render_template('index.html', friends = friends)

@app.route('/friends/<id>/delete')
def destroy(id):
            query = "DELETE FROM friends WHERE id=:id"

            data = {
            'id': id
            }

            mysql.query_db(query, data)
            return redirect('/')

@app.route('/friends', methods=['POST'])
def create():
        query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'email': request.form['email']
               }
        mysql.query_db(query, data)

        return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
        query = "SELECT * FROM friends where id=:id"

        data = {
        'id': id
        }

        friend = mysql.query_db(query, data)

        return render_template('edit_friend.html', id = id, friend = friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
        query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at= NOW() WHERE id=:id"
        data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'email': request.form['email'],
                 'id': id
               }
        mysql.query_db(query, data)
        return redirect('/')

app.run(debug=True)
