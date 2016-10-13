import random
import re
from flask import Flask, render_template, request, redirect, flash, session
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
CAP_REGEX = re.compile(r'^(?=.*[0-9]+.*)(?=.*[A-Z]+.*)[a-zA-Z0-9.+_-]+$')
DOB_REGEX = re.compile(r'^(?=.*[0-9]+.*)(?=.*[A-Z]+.*)[a-zA-Z0-9.+_-]+$')
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():

    return render_template('index.html')

@app.route("/process", methods=['POST'])
def process():
    # err=0
    if len(request.form['first_name']) < 1 or re.search('\d+', request.form['first_name']):
        flash("First name cannot be empty or contain any numbers!", 'error')
    if len(request.form['last_name']) < 1 or re.search('\d+', request.form['first_name']):
        flash("Last name cannot be empty or contain any numbers!", 'error')
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'error')
    if len(request.form['password']) < 1:
        flash("Password cannot be blank!", 'error')
    elif not CAP_REGEX.match(request.form['password']):
        flash("Password must contain ay least 1 uppercase letter and 1 numeric value", 'error')
    if request.form['confirm_password'] != request.form['password']:
        flash("Confirm Password doesn't match the Password!", 'error')
    if "_flashes" not in session:
        flash("Success, you are now registered!", 'pass')
    return redirect('/')
    # else:
    #     myName=request.form['name']
    #     myLocation=request.form['location']
    #     myLanguage=request.form['language']
    #     myComment=request.form['comment']
    #     return render_template('result.html',name=myName, location=myLocation, language=myLanguage, comment=myComment)

app.run(debug=True)
