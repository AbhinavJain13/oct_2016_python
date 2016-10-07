from flask import Flask, render_template, request, redirect, session,flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = ('secretkeyayyyy')

@app.route('/')
def index(): #beginning of function
    return render_template("index.html") #loading the index.html template

@app.route('/user', methods = ['POST']) #new route going to the localhost:5000/user
def create_user():
    print "Got Post Info"
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name'] #the request form is grabbing the 'name' from the text input INSIDE the form and setting it to name
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']

    if len(session['email']) < 1:
        flash('email: You must enter characters into the field')
    if not EMAIL_REGEX.match(request.form['email']):
        flash('email: must enter valid email')
    if len(session['first_name']) < 1:
        flash('first name: You must enter characters into the field')
    if not session['first_name'].isalpha():
        flash('You must only enter letters A-Z')
    if len(session['last_name']) < 1:
        flash('last name: You must enter characters into the field')
    if not session['last_name'].isalpha():
        flash('You must only enter letters A-Z')
    if len(session['password']) < 1:
        flash('password: You must enter characters into the field')
    if len(session['password']) < 8:
        flash("You're password must be longer than 8 characters")
    if len(session['confirm_password']) < 1:
        flash('confirm password: You must enter characters into the field')
    if session['confirm_password'] != session['password']:
        flash('The passwords should match')
    return redirect('/')

app.run(debug = True) #runs code
