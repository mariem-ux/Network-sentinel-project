from http.server import HTTPServer, SimpleHTTPRequestHandler

print("Starting DMZ web server on port 80...")
server = HTTPServer(("0.0.0.0", 80), SimpleHTTPRequestHandler)
server.serve_forever()