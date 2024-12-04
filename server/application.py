"""
This module contains the main application logic for the HTTP server.
It defines the 'TestMe' class and provides basic HTTP server functionality.
"""

import http.server
import socketserver

PORT = 8000

class TestMe:
    """A simple class for testing purposes."""

    def take_five(self):
        """Return the number 5."""
        return 5

    def port(self):
        """Return the port number."""
        return PORT


if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
