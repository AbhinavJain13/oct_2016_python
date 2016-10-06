import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path1>')
def patch1(path1):
    if "images" not in session:
        session['images'] = []
    if path1=="ninja":
        session['images'] = ["donatello.jpg","leonardo.jpg","michelangelo.jpg","raphael.jpg"]
        return render_template('ninja.html')
    else:
        session['images'] = ["notapril.jpg"]
        return render_template('ninja.html')

@app.route('/<path1>/<path2>')
def path2(path1, path2):
    if "images" not in session:
        session['images'] = []
    if path1=="ninja" and path2=="blue":
        session['images'] = ["leonardo.jpg"]
        return render_template('ninja.html')
    if path1=="ninja" and path2=="orange":
        session['images'] = ["michelangelo.jpg"]
        return render_template('ninja.html')
    if path1=="ninja" and path2=="red":
        session['images'] = ["raphael.jpg"]
        return render_template('ninja.html')
    if path1=="ninja" and path2=="purple":
        session['images'] = ["donatello.jpg"]
        return render_template('ninja.html')
    else:
        session['images'] = ["notapril.jpg"]
        return render_template('ninja.html')
app.run(debug=True)
