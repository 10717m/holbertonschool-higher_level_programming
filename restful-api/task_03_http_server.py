import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Initialize response variables
        response = ""
        content_type = "text/plain"
        status_code = 200
        
        # Handle different endpoints
        if self.path == '/':
            response = "Hello, this is a simple API!"
        elif self.path == '/data':
            response = json.dumps({"name": "John", "age": 30, "city": "New York"})
            content_type = "application/json"
        elif self.path == '/status':
            response = "OK"
        elif self.path == '/info':
            response = json.dumps({
                "version": "1.0",
                "description": "A simple API built with http.server"
            })
            content_type = "application/json"
        else:
            response = "Endpoint not found"
            status_code = 404
        
        # Send response
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
