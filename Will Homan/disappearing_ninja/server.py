from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)


@app.route('/')
def index():

  return render_template('index.html')


@app.route('/ninja', methods=['GET'])
def ninja():
    color = ""
    return render_template("ninja.html", color = color)

@app.route('/ninja/<color>', methods=['GET'])
def turtles(color):
     return render_template("ninja.html", color = color)



     return redirect('/')

app.run(debug=True)
