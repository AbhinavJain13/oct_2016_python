from flask import Flask, render_template, request, session, flash, redirect
app = Flask(__name__)
app.secret_key = ('thisissecret')

@app.route('/')
def index(): #beginning of function
    return render_template("index.html") #loading the index.html template

@app.route('/user', methods = ['POST']) #new route going to the localhost:5000/user
def create_user():
    if len(request.form['name']) < 1:
        flash('You did not enter anything!')
        return redirect('/')
    if len(request.form['comment']) > 120:
        flash("You're comment is longer than 120 characters! please shorten")
        return redirect ('/')
    else:
        return redirect('/')
    print "Got Post Info"
    name = request.form['name'] #the request form is grabbing the 'name' from the text input INSIDE the form and setting it to name
    dojo_location = request.form['dojo_location']#the request form is grabbing 'dojo_location' from the text input INSIDE the form and setting it to name
    fav_languages = request.form['fav_languages'] #same idea
    comment = request.form['comment'] #same
    #code below is printing the variables we created above

    print fav_languages
    print name
    print dojo_location
    print comment
    return render_template('result.html',  name=name, dojo_location=dojo_location, fav_languages=fav_languages, comment=comment) #this return is rendering the result.html template for the /user route stated above in the @app.route the variables are included here to "link" the variables so the html can interpret them.

app.run(debug = True) #runs code
