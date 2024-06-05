import signal
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

class GreeterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/greeter/greet":
            name = self.get_query_param("name", "Stranger")
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Hello, {name}!\n".encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Not Found\n".encode())

    def get_query_param(self, param_name, default_value):
        query_params = self.path.split("?")[1]
        for param in query_params.split("&"):
            key, value = param.split("=")
            if key == param_name:
                return value
        return default_value

def run(server_class=HTTPServer, handler_class=GreeterHandler, port=9090):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP Greeter on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("HTTP server stopped serving new requests.")

if __name__ == "__main__":
    run()
