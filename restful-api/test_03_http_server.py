import unittest
import http.client
import json

class TestSimpleAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the server in a separate process for testing
        import subprocess
        cls.server_process = subprocess.Popen(['python3', 'task_03_http_server.py'])
        
        # Give the server time to start
        import time
        time.sleep(1)
        
        # Set up connection to the server
        cls.conn = http.client.HTTPConnection('localhost', 8000)

    @classmethod
    def tearDownClass(cls):
        # Close the connection and terminate the server process
        cls.conn.close()
        cls.server_process.terminate()

    def test_root_endpoint(self):
        """Test the root endpoint (/)"""
        self.conn.request("GET", "/")
        response = self.conn.getresponse()
        
        self.assertEqual(response.status, 200)
        self.assertEqual(response.read().decode('utf-8'), "Hello, this is a simple API!")
        self.assertEqual(response.getheader('Content-type'), 'text/plain')

    def test_data_endpoint(self):
        """Test the /data endpoint"""
        self.conn.request("GET", "/data")
        response = self.conn.getresponse()
        
        self.assertEqual(response.status, 200)
        data = json.loads(response.read().decode('utf-8'))
        self.assertEqual(data, {"name": "John", "age": 30, "city": "New York"})
        self.assertEqual(response.getheader('Content-type'), 'application/json')

    def test_status_endpoint(self):
        """Test the /status endpoint"""
        self.conn.request("GET", "/status")
        response = self.conn.getresponse()
        
        self.assertEqual(response.status, 200)
        self.assertEqual(response.read().decode('utf-8'), "OK")
        self.assertEqual(response.getheader('Content-type'), 'text/plain')

    def test_info_endpoint(self):
        """Test the /info endpoint"""
        self.conn.request("GET", "/info")
        response = self.conn.getresponse()
        
        self.assertEqual(response.status, 200)
        data = json.loads(response.read().decode('utf-8'))
        self.assertEqual(data, {
            "version": "1.0",
            "description": "A simple API built with http.server"
        })
        self.assertEqual(response.getheader('Content-type'), 'application/json')

    def test_not_found_endpoint(self):
        """Test a non-existent endpoint"""
        self.conn.request("GET", "/nonexistent")
        response = self.conn.getresponse()
        
        self.assertEqual(response.status, 404)
        self.assertEqual(response.read().decode('utf-8'), "Endpoint not found")
        self.assertEqual(response.getheader('Content-type'), 'text/plain')

if __name__ == '__main__':
    unittest.main()
