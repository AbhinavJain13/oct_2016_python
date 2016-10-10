from flask import Flask, render_template, request, redirect
app = Flask(__name__)

ninjas = {
        'blue': 'leonardo.jpg',
        'red': 'raphael.jpg',
        'purple': 'donatello.jpg',
        'orange': 'michelangelo.jpg'
        }

@app.route('/')
def index():
  return render_template("index.html")
@app.route('/ninja')
def ninja():
    return render_template("ninja.html", dict=ninjas)
@app.route('/ninja/<color>')
def color(color):
    which = {}
    if color == 'blue':
        which[color] = ninjas[color]
    elif color == 'purple':
        which[color] = ninjas[color]
    elif color == 'red':
        which[color] = ninjas[color]
    elif color == 'orange':
        which[color] = ninjas[color]
    else:
        which[color] = 'notapril.jpg'
    return render_template("ninja.html", dict=which)
app.run(debug=True) # run our server
