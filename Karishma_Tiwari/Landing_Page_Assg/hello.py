from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world():
    return render_template("index.html", name = "Katy")

@app.route('/ninjas')
def info():
    return render_template("ninjas.html")

@app.route('/dojos/new')
def dojoform():
    return render_template("dojos.html")
app.run(debug = True)
