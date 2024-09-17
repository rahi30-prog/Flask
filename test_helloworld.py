import unittest
from flask import Flask

# Import the Flask app
from helloworld import app  # Replace 'your_flask_app' with the name of your file (without .py)

class FlaskTestCase(unittest.TestCase):
    # Set up the test client before running tests
    def setUp(self):
        app.testing = True  # Set testing mode
        self.client = app.test_client()  # Initialize test client

    # Test if the homepage works
    def test_hello_world(self):
        # Simulate a GET request to the "/" route
        response = self.client.get('/')
        
        # Check if the response code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response data matches the expected output
        self.assertEqual(response.data, b'<p>Hello, World!</p>')

if __name__ == '__main__':
    unittest.main()
