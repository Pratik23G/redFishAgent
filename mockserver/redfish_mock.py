import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("PATH ASKED FOR:", self.path)
        if self.path == "/redfish/v1/":
            body = json.dumps({"@odata.id": "/redfish/v1/",
                                "Name": "Root Service"}).encode()
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/redfish/v1/Systems/":
            body = json.dumps({
                    "@odata.id": "/redfish/v1/Systems",
                    "Members@odata.count": 1,
                    "Members": [
                        {"@odata.id": "/redfish/v1/Systems/1"}
                    ]
            }).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()