from flask import Flask, render_template, redirect
app= Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template('pics.html' )

@app.route('/ninja/<color>')
def turtle(color):
    name=color
    return render_template('pics.html', name=name )
app.run(debug=True)
