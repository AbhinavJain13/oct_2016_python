import random
import re
from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnector(app,'email_validation_db')

def insert():
    query = "INSERT INTO emails (email) VALUES (:email)"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'email': request.form['email']
            #  'last_name':  request.form['last_name'],
            #  'occupation': request.form['occupation']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    # email_list = mysql.query_db("SELECT * FROM emails")
    # print (email_list)

@app.route('/')
def index():
    print ("*** rendering index.html")
    return render_template('index.html')

@app.route("/process", methods=['POST'])
def validate():
    print ("*** in process")
    print (request.form['email'])
    if EMAIL_REGEX.match(request.form['email']):
        print ("*** validated")
        insert()
        emails = mysql.query_db("SELECT * FROM emails")
        print ("*** rendering success.html")
        return render_template('success.html', email=request.form['email'], useremails=emails)
    else:
        flash("Invalid Email Address!", 'error')
        print ("*** not valid")
        # for message in _flashes:
        #     print (message)
        return redirect('/')

@app.route('/success')
def success():
    emails = mysql.query_db("SELECT * FROM emails")
    print ("*** rendering success.html")
    return render_template('success.html', useremails=emails)

@app.route('/delete/<id>')
def delete(id):
    query="DELETE FROM emails WHERE id=:id"
    data= {'id':id}
    mysql.query_db(query, data)
    return redirect('/success')

app.run(debug=True)
