from flask import Flask, render_template, redirect, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route ('/data', methods=['POST'])
def data():
    print "got Post info"
    name=request.form['name']
    location=request.form['dojo']
    language=request.form['language']
    comments=request.form['comments']
    return render_template('submitted.html',name=name, location=location, language=language, comments=comments )
@app.route('/submit')
def submit():
    return render_template('submitted.html')
app.run(debug=True)
