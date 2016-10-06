from flask import Flask, render_template, session, redirect, request

app=Flask(__name__)
app.secret_key="Dontaskmeforkeys"

@app.route('/')
def home():
    empty = "No ninjas here"
    return render_template('index3.html',empty="No ninjas here")

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')


@app.route('/<firstword>/<keyword>')
def show_them(firstword,keyword):
    session['keyword'] = keyword
    return render_template('index3.html', firstword = firstword)

app.run(debug=True)
