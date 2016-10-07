from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    Location = request.form['Location']
    Language = request.form['Language']
    comment = request.form['comment']
    return render_template('results.html', name=name, Location=Location, Language=Language, comment=comment)

app.run(debug=True)
