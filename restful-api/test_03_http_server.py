#!/usr/bin/env python3
import unittest
import subprocess
import time
import requests

class TestSimpleAPI(unittest.TestCase):
    base_url = 'http://localhost:8000'

    @classmethod
    def setUpClass(cls):
        # Start the server in background
        cls.server_process = subprocess.Popen(['python3', 'task_03_http_server.py'])
        time.sleep(1)  # Give the server time to start

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()
        cls.server_process.wait()

    def test_root_endpoint(self):
        r = requests.get(f"{self.base_url}/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "Hello, this is a simple API!")

    def test_data_endpoint(self):
        r = requests.get(f"{self.base_url}/data")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertEqual(r.json(), {"name": "John", "age": 30, "city": "New York"})

    def test_status_endpoint(self):
        r = requests.get(f"{self.base_url}/status")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "OK")

    def test_undefined_endpoint(self):
        r = requests.get(f"{self.base_url}/undefined")
        self.assertEqual(r.status_code, 404)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertEqual(r.json(), {"error": "Endpoint not found"})

if __name__ == "__main__":
    unittest.main()

