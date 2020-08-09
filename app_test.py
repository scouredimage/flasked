from flask_testing import TestCase
from .app import app

class MyTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_server_is_up_and_running(self):
        response = self.client.get('/hello/ollie')
        self.assertEqual(response.data, b'Hello ollie!')

