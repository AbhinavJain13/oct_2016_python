
from flask import Flask, redirect, render_template, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    allninjas = True
    return render_template('ninja.html',allninjas = allninjas)

@app.route('/ninja/<color>')
def color(color):
    allninjas = False
    return render_template('ninja.html', allninjas=allninjas, color = color)

app.run(debug=True)
