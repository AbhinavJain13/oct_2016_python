from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-z]+$')

app = Flask(__name__)
app.secret_key= 'secretkey'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['post'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if len(request.form['first_name']) < 1 or not NAME_REGEX.match(request.form['first_name']):
        flash("First and last names must be alphabetic and may not be left blank")
        return redirect('/')
    elif len(request.form['last_name']) < 1 or not NAME_REGEX.match(request.form['last_name']):
        flash("First and last names must be alphabetic and may not be left blank")
        return redirect('/')
    elif len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']):
        flash("WRONG. Use a real email.")
        return redirect('/')
    elif len(request.form['password']) < 8:
        flash("Passwords must be at least 8 characters")
        return redirect('/')
    elif request.form['password'] != request.form['confirm_password']:
        flash("Confirm password must be the same as password how do you not get this by now?")
        return redirect('/')
    else:
        flash("Thanks for submitting your information. Your parents will be returned to you shortly.")
        return redirect('/')

app.run(debug=True)
