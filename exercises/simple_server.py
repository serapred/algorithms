"""
a simple python server using std library http
"""

from http.server import HTTPServer, BaseHTTPRequestHandler


# custom wrapper
class Serv(BaseHTTPRequestHandler):

    # inherited
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            # open file in cwd
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        # render page
        self.wfile.write(bytes(file_to_open, 'utf-8'))


if __name__ == '__main__':

    httpd = HTTPServer(('localhost', 8080), Serv)
    httpd.serve_forever()
