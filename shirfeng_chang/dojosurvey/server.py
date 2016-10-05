#!/usr/bin/env python
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def user():
    name = request.form['name']
    loc = request.form['loc']
    lang = request.form['lang']
    comment = request.form['comment']
    return render_template("results.html", name=name, loc=loc, lang=lang, comment=comment)
    return redirect('/')
app.run(debug=True) # run our server
