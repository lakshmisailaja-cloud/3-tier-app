from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("""
<html>
<body>
<h1>Backend Running Successfully</h1>
<h2>AWS DevOps 3 Tier Project</h2>
</body>
</html>
""", "utf-8"))

server = HTTPServer(("0.0.0.0", 5000), MyServer)
print("Server running on port 5000")
server.serve_forever()
