from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/result', methods=['POST'])
def create_users():
    print request.form
    name = request.form['name']
    location= request.form['location']
    lang=request.form['lang']
    comment=request.form['comments']
    return render_template("result.html",name=name,Location=location,lang=lang,comments=comment)
    return redirect('/')
app.run(debug=True)
