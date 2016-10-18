from flask import Flask, render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template('survey.html')

@app.route('/result',methods=['POST'])
def result():
    name = request.form['name']
    place = request.form['place']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('results.html', name = name, place=place, language=language,comment=comment)
    return redirect('/result')
app.run(debug=True)
