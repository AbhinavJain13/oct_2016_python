from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # take care of senstive info
# localhost5000

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/process')
