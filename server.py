from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print('Starting server on port 8000...')
httpd.serve_forever()
