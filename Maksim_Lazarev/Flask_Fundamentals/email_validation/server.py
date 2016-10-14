import random
import re
from flask import Flask, render_template, request, redirect, flash, session
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():

    return render_template('index.html')

@app.route("/process", methods=['POST'])
def process():
    # err=0
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'error')
    if "_flashes" not in session:
        flash("The email address you entered ("
        +request.form['email']+") is a VALID email address! Thank you!", 'pass')
    return redirect('/')
    # else:
    #     myName=request.form['name']
    #     myLocation=request.form['location']
    #     myLanguage=request.form['language']
    #     myComment=request.form['comment']
    #     return render_template('result.html',name=myName, location=myLocation, language=myLanguage, comment=myComment)

app.run(debug=True)
