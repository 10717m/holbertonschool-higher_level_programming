import unittest
import requests
import subprocess
import time
import os

class TestBasicAuthNoCredentials(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the Flask server in a separate process
        cls.server_process = subprocess.Popen(
            ['python3', 'task_05_basic_security.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # Give the server time to start
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # Terminate the server process
        cls.server_process.terminate()
        cls.server_process.wait()

    def test_basic_auth_no_credentials(self):
        """Test accessing basic-protected endpoint without credentials"""
        url = 'http://localhost:5000/basic-protected'
        
        # Make request without any authentication
        response = requests.get(url)
        
        # Verify status code is 401
        self.assertEqual(response.status_code, 401, 
                         "Should return 401 Unauthorized when no credentials provided")
        
        # Verify the response contains the expected error message
        response_data = response.json()
        self.assertIn('error', response_data, 
                      "Response should contain 'error' field")
        self.assertEqual(response_data['error'], 'Unauthorized',
                         "Error message should be 'Unauthorized'")

    def test_basic_auth_with_credentials(self):
        """Test accessing basic-protected endpoint with valid credentials"""
        url = 'http://localhost:5000/basic-protected'
        
        # Make request with valid credentials
        response = requests.get(url, auth=('user1', 'password'))
        
        # Verify status code is 200
        self.assertEqual(response.status_code, 200, 
                         "Should return 200 OK when valid credentials provided")
        
        # Verify the response contains the success message
        response_data = response.json()
        self.assertIn('message', response_data, 
                      "Response should contain 'message' field")
        self.assertEqual(response_data['message'], 'Basic Auth: Access Granted',
                         "Success message should match expected")

if __name__ == '__main__':
    unittest.main()
