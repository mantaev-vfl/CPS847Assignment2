import unittest
from flask_api import app

class TestFlaskApp(unittest.TestCase):
    def test_statusCode(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
