import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # myGreeting="Greetings from Flask!"
    # myNumber = random.randint(1,99)
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def result():
    myName=request.form['name']
    myLocation=request.form['location']
    myLanguage=request.form['language']
    myComment=request.form['comment']
    return render_template('result.html',name=myName, location=myLocation, language=myLanguage, comment=myComment)

# @app.route("/dojos/new")
# def dojos():
#     myDojoGreeting="DoJo Greeting!"
#     return render_template('dojos.html',greeting=myDojoGreeting)
app.run(debug=True)
