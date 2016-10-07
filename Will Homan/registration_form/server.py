from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():

  return render_template('index.html')


@app.route('/process', methods=['Post'])
def process():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    if len(request.form['first_name']) < 1:
          flash("First Name cannot be blank!")
    if len(request.form['last_name']) < 1:
        flash("Last Name cannot be blank!")
    if len(request.form['password']) < 1:
            flash("Password cannot be blank!")
    if len(request.form['confirm_password']) < 1:
            flash("Confirm Password cannot be blank!")
    if str.isalpha(request.form['first_name']) == False:
        flash("Last Name cannot contain a number!")
    if str.isalpha(request.form['last_name']) == False:
        flash("Last Name cannot contain a number!")
    if len(request.form['password']) > 8:
        flash("Password cannot contain more than 8 charecters!")
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    if request.form['confirm_password'] != request.form['password']:
        flash("Passwords do not match!")
    else:
        flash("Thanks for submitting your information.")

    return redirect('/')

app.run(debug=True)
