from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html')

@app.route('/ninjas/<color>')
def turtle(color):
    return render_template('color.html', color = color)

app.run(debug = True)
