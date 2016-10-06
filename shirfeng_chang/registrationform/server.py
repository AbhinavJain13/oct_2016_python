#!/usr/bin/env python
import re
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

name_regex=re.compile(r'^[a-zA-Z.]+$')
email_regex=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def user():
    session["email"] = request.form['email']
    session["first"] = request.form['first']
    session["last"] = request.form['last']
    session["pass"] = request.form['pass']
    session["passconfirm"] = request.form['passconfirm']

    if len(session["email"]) < 1 or len(session["first"]) < 1 or len(session["last"]) < 1 or len(session["pass"])  < 1 or len(session["passconfirm"]) < 1:
        flash("One or more required fields are empty")
        return redirect('/')
    elif not email_regex.match(request.form["email"]):
        flash("Invalid e-mail")
        return redirect('/')
    elif not (name_regex.match(request.form["first"]) or name_regex.match(request.form["last"])):
        flash("First and last name should not contain numbers")
        return redirect('/')
    elif len(session["pass"]) <= 8:
        flash("Password should be more than 8 characters")
        return redirect('/')
    elif len(session["pass"]) != len(session["passconfirm"]):
        flash("Passwords do not match")
        return redirect('/')
    else:
        return render_template("results.html")
    return redirect('/')
app.run(debug=True) # run our server
