from flask import Flask
app = Flask(__name__)

@app.route('localhost:5000/')

def hello.world():
    return 'Hello World!'
app.run(debug = True)
