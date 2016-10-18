from flask import Flask, render_template, flash, redirect, request, session
import re
app = Flask(__name__)
app.secret_key='thisisasecretsecretkey'

from mysqlconnection import MySQLConnector

mysql = MySQLConnector(app, 'friends')
EREG = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
#email validator

@app.route('/')
def index():
            query = "SELECT * FROM friends"
            table = mysql.query_db(query)
            return render_template('index.html', table=table)

# @app.route('/friends', methods = ['GET','POST'])
# def routing():
#     return render_template('/friends.html')

@app.route('/friends', methods=["post"])
def submission():
    if not EREG.match(request.form['email']):     # act of validating
        flash("Get rekt")
        return redirect('/')

    else:

        data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'email': request.form['email']
               }

        query = "INSERT INTO friends(first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
        infor = mysql.query_db(query, data)

        query = "SELECT * FROM friends"
        updated = mysql.query_db(query)
        return render_template('/friends.html', updated=updated)
        #return redirect('/friends') or redirect('/home')

@app.route('/friends/<id>/edit', methods=['post'])
def update_entry(id):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id,
    }
    query = "UPDATE friends(first_name, last_name, email, updated_at) VALUES(:first_name, :last_name, :email, NOW()) WHERE friends.id=:id"

    updated_entry = mysql.query_db(query, data)

    return render_template('edit.html')

@app.route('/friends/<id>')
def placeholder(id):

    return render_template('friends.html')

@app.route('/friends/<id>/delete')
def delete_entry(id):

    return render_template('friends.html')

app.run(debug=True)
