from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time
from socketserver import ThreadingMixIn
import threading

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(10)
        message = threading.currentThread().getName()
        print(message)
        list_e = [f for f in os.listdir("."+self.path)]
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<ul>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</ul>", "utf-8"))
        for name in list_e:
            self.wfile.write(bytes(f'<li><a href="{name}">{name}</a></li>', "utf-8"))
        self.wfile.write(bytes("</ul>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    pass


if __name__ == "__main__":
    webServer = ThreadedHTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
