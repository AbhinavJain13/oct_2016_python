import random
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    name = "Dan"
    random_num = random.randint(1,99)
    return render_template("index.html", name=name, random_num=random_num)

app.run(debug=True)
