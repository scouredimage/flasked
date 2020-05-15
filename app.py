from flask import Flask
from flask_testing import TestCase

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

class MyTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_server_is_up_and_running(self):
        response = self.client.get('/hello/ollie')
        self.assertEqual(response.data, b'Hello ollie!')

