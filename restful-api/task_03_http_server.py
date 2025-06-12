import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set response headers
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        
        # Handle different endpoints
        if self.path == '/':
            response = "Hello, this is a simple API!"
            self.send_header('Content-type', 'text/plain')
        elif self.path == '/data':
            response = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.send_header('Content-type', 'application/json')
        elif self.path == '/status':
            response = "OK"
            self.send_header('Content-type', 'text/plain')
        elif self.path == '/info':
            response = json.dumps({
                "version": "1.0",
                "description": "A simple API built with http.server"
            })
            self.send_header('Content-type', 'application/json')
        else:
            self.send_response(404)
            response = "Endpoint not found"
            self.send_header('Content-type', 'text/plain')
        
        # End headers and send response
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
