from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = 'pwmf'


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0;
    session['count'] += 1
    return render_template('index.html')

@app.route('/2', methods = ['GET'])
def ninja():
    session['count'] += 1;
    return redirect('/')
    return render_template('index.html')

@app.route('/reset', methods = ['GET'])
def hacker():
    session['count'] = 0;
    return redirect('/')
    return render_template('index.html')
app.run(debug=True)
