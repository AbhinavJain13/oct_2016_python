import random
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    # myGreeting="Greetings from Flask!"
    # myNumber = random.randint(1,99)
    return render_template('index.html')

@app.route("/process", methods=['POST'])
def process():
    err=0
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        err=1
    if len(request.form['comment']) < 1 or len(request.form['comment']) >120:
        flash("Comment should be within 1-120 characters!")
        err=1
    if err==1:
        return redirect('/')
    else:
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
