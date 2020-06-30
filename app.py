from flask import Flask, Blueprint, request
from flask.views import View
from flask.views import MethodView
import json

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

class HelloView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        return "Hello with a view!"

app.add_url_rule('/views/', view_func=HelloView.as_view('view_api'))

bp = Blueprint('api', __name__, url_prefix='/api/')
bp.route('')
class HelloMethodView(MethodView):
    def get(self, name):
        return "Method hello %s!" % name

    def put(self):
        name = json.loads(request.data)['name']
        return "Method hello %s!" % name

hello_method_view = HelloMethodView.as_view('method_view_api')
bp.add_url_rule('/methodviews/', defaults={'name': 'anonymous'}, view_func=hello_method_view, methods=['GET',])
bp.add_url_rule('/methodviews/<name>', view_func=hello_method_view, methods=['GET',])
bp.add_url_rule('/methodviews/', view_func=hello_method_view, methods=['PUT',])
app.register_blueprint(bp)

