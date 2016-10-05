from flask import Flask, render_template, redirect,request, session
import random
app=Flask(__name__)
app.secret_key="hot_dog"


@app.route("/")
def number():
    session['number']= random.randrange(1,101)
    print(session['number'])
    return render_template('index.html',num1=session['number'])
def index():
    # num=request.form['num']
    return render_template('index.html')
    # return redirect('/')
@app.route ('/data', methods=['POST'])
def data():
    try:
        session['num']=int(request.form['num'])
    except ValueError:
        return render_template('guess_again.html', num=session['num'], happy=session['number'])

    return  render_template('guess_again.html', num=session['num'], happy=session['number'])
@app.route('/clear', methods=['POST'])
def clear():
    print("CLEARED!")
    session.pop('num')
    session.pop('number')
    return redirect('/')

app.run(debug=True)
