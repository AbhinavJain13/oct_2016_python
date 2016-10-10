from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
import random
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    if 'number1' not in session:
    # session['number1']=50
        session['number1']=random.randint(40,101)
    print session['number1']

    return render_template("index.html")

@app.route('/users', methods=['POST'])
def check():
        print request.form
        session['numbers']=int(request.form ['number'])
        # return render_template('index.html',number=session['numbers'])
        return redirect('/')
@app.route('/restart', methods=['POST'])
def Play_again():
    session.clear()
    # if "number1" in session:
    #     session.pop('number1')
    #
    # # secretnumber()
    session['number1']=random.randint(40,101)
    return redirect('/')
    # return render_template('index.html')



app.run(debug=True)
