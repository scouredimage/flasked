from flask import Flask
app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return "Hello %s!" % name

@app.route("/goodbye/<name>")
def goodbye(name):
    return "Goodbye %s!" % name

@app.route("/howdy/<name>")
def howdy(name):
    raise Exception('how do?')
