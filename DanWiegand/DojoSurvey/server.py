from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'secret_key'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
  # name = request.form['name']
  # location = request.form['location']
  # language = request.form['language']
  # comment = request.form['comment']
  # return redirect('/results')

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    if len(request.form['name']) < 1:
        flash('Name cannot be empty!')
    else:
        flash('Name Success!')
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(request.form['comment']) < 1:
        flash('Comment cannot be empty!')
    elif len(request.form['comment']) > 120:
        flash('Comment cannot be more than 120 characters!')
    else:
        flash('Comment Success!')
    return render_template("return.html", name=name, location=location, language=language, comment=comment)
    # return redirect('/results')

app.run(debug=True) # run our server
