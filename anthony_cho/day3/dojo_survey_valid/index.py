from flask import Flask, render_template, request, redirect,session,  flash
app = Flask(__name__)
app.secret_key = 'SecretCode'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process', methods=["POST"])
def process():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    elif len(request.form['comment']) > 120:
        flash("Comment too long")
    else:
        flash("Name: {}".format(request.form['name']))
        flash("Location: {}".format(request.form['location']))
        flash("Favorite Language: {}".format(request.form['language']))
        flash("Comments: {}".format(request.form['language']))
    return redirect('/result')

@app.route('/result')
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms

   return render_template("results.html")
app.run(debug=True) # run our server
