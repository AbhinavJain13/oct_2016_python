from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])[a-zA-Z\d]+$')
  #.is not working
app = Flask(__name__)
app.secret_key = 'Shh'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def valid():
    if len(request.form["first_name"]) < 1:
        flash("Name/password/email/password/confirm_password/ cannot be empty!")
        return redirect('/')

    # elif not str.isalpha(request.form["first_name"]):
    #     flash("Numbers not allowed in first name")
    #     return redirect('/')
    #
    # elif not str.isalpha(request.form["last_name"]):
    #     flash("Numbers not allowed in last name")
    #     return redirect('/')

    elif len(request.form["password"])> 8:
        flash("Password cannot be longer than 8 characters")
        return redirect('/')

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Enter a valid email")
        return redirect('/')

    elif not str(request.form["password"])== str(request.form["confirm_password"]):
        flash("Password do not match")
        return redirect('/')
    else:
        flash("Thanks for submitting your information.")
        return redirect('/')




app.run(debug=True)
