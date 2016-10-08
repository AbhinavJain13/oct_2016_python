from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
import random
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    if 'gold' not in session:
            # session['number1']=50
        session['gold']=0
    if 'buildings' not in session:
        session['buildings']=0
    if 'activities' not in session:
        session['activities']=""

    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
        buildings={
                     "farm":random.randint(10,20),
                     "cave":random.randint(5,10),
                     "House":random.randint(2,5),
                     "Casino":random.randint(0,50)
                     }
        str1= str(buildings[request.form['building']])
        act =request.form['building']
        if act == "Casino":
            num=random.random()
            num_round=round(num)
            print num_round
            if num_round == 0:
                session['activities']=session['activities']+"lost"+str1+"gold from the"+act+"!\n"

                session['gold']=session['gold']-buildings[request.form['building']]
            else:
                session['activities']=session['activities']+"Earned"+str1+"gold from the"+act+"!\n"
                session['gold']=session['gold']+buildings[request.form['building']]
        else:
            session['activities']=session['activities']+"Earned"+str1+"gold from the"+act+"!\r\n"
            session['gold']=session['gold']+buildings[request.form['building']]

        print session['activities']


        # return render_template('index.html',gold=session['gold'],activity=session['activities'])
        return redirect('/')


app.run(debug=True)
