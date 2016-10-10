from flask import Flask,render_template,request,redirect,session

# the server is listening here
# localhost:5000/users
app = Flask(__name__)
app.secret_key="OnlyInAJeep"
# default route
@app.route("/")
def index():
    name = "Erik"
    range=5
    return render_template("html/index.html",name=name,times=5)
# users
@app.route("/users", methods=['POST'])
def create_user():
    print "Got POST"
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    # after a post is processed, redirect....
    return redirect('/show')
# show
@app.route("/show")
def show():
    return render_template('html/user.html')


app.run(debug=True)
