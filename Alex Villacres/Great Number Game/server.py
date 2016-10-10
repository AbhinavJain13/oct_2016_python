from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = ('thisisasecret')

@app.route('/')
def index():
    if 'secret' not in session:
        session['secret'] = random.randrange(0, 101)
    print(session['secret'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    print("CLEARED!")
    del session['secret']
    del session['guess']
    return redirect('/')

app.run(debug=True)
