from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# main page and counter
@app.route('/')
def index():
    try:
        session['count'] += 1
    except:
        session['count'] = 1
    return render_template("index.html")
@app.route('/add2', methods=['POST'])
def add2():
    session['count'] += 1
    return redirect('/')
# this route will handle clear form submission
@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

app.run(debug=True) # run our server
