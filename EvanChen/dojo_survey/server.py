from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   location = request.form['locations']
   language = request.form['languages']
   # redirects back to the '/' route
   return render_template('results.html', name=name, location=location, language=language)

@app.route('/users', methods=['POST'])
def create_user2():
   print "Got Post Info"
   # here we add two properties to session to store the name and email
   session['name'] = request.form['name2']
   session['email'] = request.form['email']
   return redirect('/show') # noticed that we changed where we redirect to so that we can go to the page that displays the name and email!

@app.route('/show')
def show_user():
  return render_template('users.html')

app.run(debug=True)
