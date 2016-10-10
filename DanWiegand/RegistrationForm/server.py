# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/return', methods=['POST'])
def submit():
    email = request.form['email']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    password = request.form['password']
    confirm = request.form['confirm']

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    # else if email doesn't match regular expression display an "invalid email address" message
    if len(request.form['firstname']) < 1:
        flash("Name cannot be blank!")
    elif not unicode.isalpha(request.form['firstname']):
        flash("Name cannot contain numbers!")
    if len(request.form['lastname']) < 1:
        flash("Name cannot be blank!")
    elif not unicode.isalpha(request.form['lastname']):
        flash("Name cannot contain numbers!")
    if len(request.form['password']) < 8:
        flash("Password must be 8 or more characters!")
    if len(request.form['confirm']) < 1:
        flash("Password cannot be blank!")
    elif request.form['confirm'] != request.form['password']:
        flash("Passwords do not match!")
    else:
        flash("Your password is set!")
    return render_template('return.html', email=email, firstname=firstname, lastname=lastname)
app.run(debug=True)
