from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'SecretCode'  # you need to set a secret key for security purposes
# main page and counter


@app.route('/')
def index():
    # checks if session["gold"] is created yet
    if 'gold' not in session:
        session['gold'] = 0
        print('started new game')
    if 'activities' not in session:
        session['activities'] = []
    return render_template("index.html")


@app.route('/process_money', methods=['POST'])
def process_money():
    buildings = {
        'farm': random.randint(10, 20),
        'cave':random.randint(5, 10),
        'house': random.randint(2, 5),
        'casino': random.randint(-50, 50)
    }
    #current time and date
    date = datetime.datetime.now()
    print(request.form['building'])
    #checks if type of building is in the building object holding my gold
    if request.form['building'] in buildings:
        #adds to the gold at the top
        result = buildings[request.form['building']]
        session['gold'] += result
        not_casino = "Earned {} golds from the {}!".format(result, request.form['building'])
        casino = "Entered a casino and {} {} golds.{}".format("won" if result > 0 else "lost", result if result > 0 else -result, " Yay!" if result > 0 else ".. Ouch..")
        result_dict = {
            'class': 'green' if result > 0 else "red",
            'activity': not_casino if request.form['building'] != 'casino' else casino,
            'date': date
        }
        session['activities'].append(result_dict)
    return redirect('/')

# resets the game
@app.route('/reset', methods=['POST'])
def reset():
    print("Resetting game")
    del session['gold']
    del session['activities']
    return redirect('/')
app.run(debug=True)  # run our server
