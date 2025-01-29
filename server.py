import argparse
import random
from http.server import HTTPServer, SimpleHTTPRequestHandler

parser = argparse.ArgumentParser(description="Start a restricted HTTP server.")
parser.add_argument("--bind", type=str, required=True, help="IP to bind the server.")
parser.add_argument("--allow", type=str, required=True, help="Comma-separated list of allowed IPs.")

args = parser.parse_args()
allowed_ips = set(args.allow.split(","))

port = random.randint(2000, 65000)

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        if client_ip not in allowed_ips:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"403 Forbidden")
            return

        super().do_GET()

server = HTTPServer((args.bind, port), CustomHandler)
print(f"Serving on {args.bind}:{port}, allowing only {allowed_ips}")
server.serve_forever()
