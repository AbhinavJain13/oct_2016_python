from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dojo_survey_index.html')

@app.route('/result', methods=['POST'])
def create_user():
    print "Got User Info!"
    name = request.form['name']
    email = request.form['email']
    comment = request.form['comment']
    location = request.form['location']
    language = request.form['language']
    print name
    print email
    print comment
    print location
    print language
    # return render_template("dojo_survey_user.html")
    return render_template('dojo_survey_result.html', name = name, email = email, comment = comment, location = location, language = language)

app.run(debug = True)
