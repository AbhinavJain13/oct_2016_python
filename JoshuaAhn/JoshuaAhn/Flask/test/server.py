from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # take care of senstive info
# localhost5000
@app.route('/')
def index():

    return render_template("index.html")
#new page to take in info
@app.route('/2visits', methods=['POST'])
def visit():
    session['count'] += 1
    return redirect('/')
# for hackers
@app.route('/clear', methods=['POST'])
def hack():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
