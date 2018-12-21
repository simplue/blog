import socket
from socketserver import BaseRequestHandler, TCPServer

SEPARATOR = '\r\n'
MAX_PACKET = 1024


# https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
# server-demo: https://stackoverflow.com/a/10114266
class EchoHandler(BaseRequestHandler):
    def send(self, data):
        self.request.send(data if isinstance(data, bytes) else data.encode())

    def set_headers(self, headers):
        self.send((SEPARATOR.join('{}: {}'.format(k, v) for k, v in headers.items())))

    def send_status(self, status_code=200, http_protocol_version='1.1'):
        assert http_protocol_version in ['1.0', '1.1']
        _status_code = int(status_code)
        status_desc = {
            200: 'OK',
            404: 'Not Found',
        }.get(_status_code, 'WTF?!')
        self.send(f'HTTP/{http_protocol_version} {_status_code} {status_desc}')

    def send_separator(self):
        self.send(2 * SEPARATOR)

    def response(self, body):
        self.send_status()
        self.set_headers({
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': len(body),
            'Connection': 'close',
        })
        self.send_separator()
        self.send(body)

    def get_raw_request(self):
        self.request.settimeout(0.1)
        req_data = []
        while True:
            try:
                chunk = self.request.recv(MAX_PACKET).decode().strip()
                req_data.append(chunk)
            except socket.timeout:
                return ''.join(req_data)

    def parse_request(self):
        raw_req = self.get_raw_request()
        if not raw_req:
            return

        try:
            head, body = raw_req.split(2 * SEPARATOR, 1)
        except ValueError:
            head, body = raw_req, None

        first_line, raw_headers = head.split(SEPARATOR, 1)
        method, route, protocol = first_line.split(' ')
        headers = { i.split(': ', 1)[0]: i.split(': ', 1)[1] for i in raw_headers.split(SEPARATOR)}

        return {
            'headers': headers,
            'method': method,
            'route': route,
            'protocol': protocol,
            'body': body,
        }

    def handle(self):
        req = self.parse_request()
        if req is None:
            return self.response('')
        if req == '/':
            return self.response('<html><body><h1>Hello, world!</h1></html>')
        # return self.response('<html><body><h1>Hello, world!</h1></html>', status=404)
        print(req['protocol'][-2:])
        self.send_status(status_code=404, http_protocol_version=req['protocol'][-2:])
        self.send_separator()
        self.send('<html><center><h1>Not Found</h1></center></html>')


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
