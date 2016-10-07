from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ninjas/<ninja_color>', methods=['get'])
def show_ninja(ninja_color):
    return render_template("notindex.html", ninja_color=ninja_color)

@app.route('/ninjas/', methods=['get'])
def noninja():
    return render_template("notindex.html", ninja_color='')

app.run(debug=True)
