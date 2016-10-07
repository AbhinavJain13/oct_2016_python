from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key ="sshh"
@app.route('/')
def show1():
    return render_template("home.html")

@app.route('/ninja/<ninja_color>', methods=['get'])
def show_ninja(ninja_color):
    return render_template("ninja.html", ninja_color=ninja_color)

@app.route('/ninja')
def show_all():
    return render_template("ninja.html", ninja_color = '')
app.run(debug=True)
