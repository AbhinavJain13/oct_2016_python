from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'mydb')
@app.route('/')
def index():

    return render_template('index.html')


@app.route('/email', methods=['Post'])
def emailcheck():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        query = "INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"

        data = {
                 'email': request.form['email'],

               }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        return redirect('/success')


@app.route('/success')
def success():
    query = "SELECT * FROM email"


    emails = mysql.query_db(query)
    return render_template('success.html', emails = emails)

@app.route('/delete/<id>')
def destroy(id):
    query = "DELETE FROM email WHERE id=:id"

    data = {
    'id': id
    }

    mysql.query_db(query, data)
    return redirect('/success')

app.run(debug=True)
