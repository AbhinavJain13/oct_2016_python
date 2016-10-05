from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user', methods = ['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    dojo_location = request.form['dojo_location']
    fav_languages = request.form['fav_languages']
    comment = request.form['comment']

    print fav_languages
    print name
    print dojo_location
    print comment
    return render_template('result.html',  name=name, dojo_location=dojo_location, fav_languages=fav_languages, comment=comment)

app.run(debug = True)
