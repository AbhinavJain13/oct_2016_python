from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of dojosurvey.py below

@app.route('/')
def dojosurvey():
    return render_template("dojosurvey.html")
# this route will render the page returned

@app.route("/user", methods=['POST'])
def create_user():


    if len(request.form['name']) < 1:
        flash("You must enter a name!")
    elif len(request.form['textbox']) < 6:
        flash("Sorry 6 char limit")
    else:
        flash("name: {}".format(request.form['name']))
        flash("location: {}".format(request.form['location']))
        flash("lang: {}".format(request.form['lang']))
        flash("textbox: {}".format(request.form['textbox']))

    return redirect('/show')

@app.route('/show')
def show_user():
    print "Thank You"

    return render_template('users.html')
app.run(debug=True)
