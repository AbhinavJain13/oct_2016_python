from flask import Flask, render_template,request,redirect, flash
import re
import getpass
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
passwordRegex = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}")

app = Flask(__name__)
app.secret_key = 'pwmf'

@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/reg',methods=['POST'])
def result():
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    pw = request.form['pw']
    conpw = request.form['conpw']
    if len(name) == 0 or len(lastname) == 0 or len(email) ==0 or len(pw) ==0 or len(conpw) == 0:
        flash("you can't leave anything blank!")
        return redirect('/')
    elif  len(name) < 1 or name.isalpha:
        flash('First name needs to be more than 1 letter and no numbers.')
        return redirect('/')
    elif len(lastname) < 1 or name.isalpha:
        flash('last to be more than 1 letter and no numbers.')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address! (example. abc123@dfe.com)')
        return redirect('/')
    elif not passwordRegex.match(request.form['email']):
        flash('You need at least 1 special character, 1 uppercase, and numeric value')
        return redirect('/')
    elif not pw == conpw:
        flash('Password does not match confirmation.')
        return redirect('/')
    elif not len(pw) > 8 and len(conpw) > 8:
        flash('PW is not over 8 characters')
    else:
        flash('Successful!')
        return redirect("/results")
    return render_template('result.html', name = name, lastname=lastname,email=email,pw=pw)
    return redirect('/')
app.run(debug=True)
