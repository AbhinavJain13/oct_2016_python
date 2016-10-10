#!/usr/bin/env python
import re
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    blue = 1
    red = 1
    orange = 1
    purple = 1
    return render_template("ninja.html", blue=blue,red=red,orange=orange,purple=purple)
    return redirect('/')

@app.route('/ninja/<arg>')
def color(arg):
    blue, orange, red, purple, other = 0,0,0,0,0
    if arg == "blue":
        blue = 1
    elif arg == "orange":
        orange = 1
    elif arg == "red":
        red = 1
    elif arg == "purple":
        purple = 1
    else:
        other = 1

    return render_template("ninja.html",blue=blue, orange=orange, red=red, purple= purple, other=other )
app.run(debug=True) # run our server
