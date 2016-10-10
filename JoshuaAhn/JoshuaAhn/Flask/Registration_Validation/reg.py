from flask import Flask, render_template, request, redirect,session,  flash
import re
app = Flask(__name__)
app.secret_key = 'SecretCode'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_check = re.compile(r'\d')

# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process', methods=["POST"])
def process():
    if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['confirm_password']) < 1 or len(request.form['password']) < 9:
        flash("You need to fill in each blank in order to continue")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email")
    elif name_check.search(request.form['first_name']) or name_check.search(request.form['last_name']):
        flash("Letters only, sorry")
    elif request.form['password'] != request.form['confirm_password']:
        flash("Password must match")
    else:
        flash("Thank you for signing up")
    return redirect('/result')

@app.route('/result')
def create_user():
   print "Got Post Info"


   return render_template("results.html")
app.run(debug=True) # run our server
