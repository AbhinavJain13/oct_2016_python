import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    myGreeting="Greetings from Flask!"
    # myNumber = random.randint(1,99)
    return render_template('index.html',greeting=myGreeting)

@app.route("/ninjas")
def ninjas():
    myNinjaGreeting="Ninja Greeting!"
    return render_template('ninjas.html',greeting=myNinjaGreeting)

@app.route("/dojos/new")
def dojos():
    myDojoGreeting="DoJo Greeting!"
    return render_template('dojos.html',greeting=myDojoGreeting)
app.run(debug=True)
