
# Dont count this file as part of the lab

import http.server
import socketserver
import shutil
from io import BytesIO


class hh(http.server.BaseHTTPRequestHandler):
    def copyfile(self, source, outputfile):
        shutil.copyfileobj(source, outputfile)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        f = BytesIO()
        f.write("OK".encode("utf8"))
        f.seek(0)
        if f:
            self.copyfile(f, self.wfile)
            f.close()


PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
