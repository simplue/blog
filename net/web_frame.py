import socket
import logging
from socketserver import BaseRequestHandler, TCPServer

SEPARATOR = '\r\n'
MAX_PACKET = 1024

FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel('INFO'.upper())

# https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
# server-demo: https://stackoverflow.com/a/10114266
class BaseHandler(BaseRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handlers = user_handlers

    def send(self, data):
        self.request.send(data if isinstance(data, bytes) else data.encode())

    def set_headers(self, headers):
        self.send_separator()
        self.send(SEPARATOR.join('{}: {}'.format(k, v) for k, v in headers.items()))

    def send_status(self, status_code=200, http_protocol_version=None):
        http_protocol_version = \
            http_protocol_version or '1.1'
        assert http_protocol_version in ['1.0', '1.1']
        _status_code = int(status_code)
        status_desc = {
            200: 'OK',
            301: 'Move Permanently',
            302: 'Found',
            404: 'Not Found',
            405: 'Method Not Allowed',
        }.get(_status_code, 'WTF?!')
        self.send(f'HTTP/{http_protocol_version} {_status_code} {status_desc}')

    def send_separator(self, count=1):
        self.send(count * SEPARATOR)

    def response(self, body):
        self.send_status()
        self.set_headers({
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': len(body),
            'Connection': 'close',
        })
        self.send_body(body)

    def send_body(self, body):
        self.send_separator(2)
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

    def send_error(self, status_code, body=''):
        assert int(status_code) > 399
        self.send_status(status_code=status_code)
        self.send_body('<html><center><h1>Not Found</h1></center></html>')

    def send_error_404(self):
        self.send_error(404, '<html><center><h1>Not Found</h1></center></html>')

    def send_error_405(self):
        self.send_error(405, '<html><center><h1>Method Not Allowed</h1></center></html>')

    def send_error_500(self):
        self.send_error(500, '<html><center><h1>Server Error</h1></center></html>')

    def redirect(self, url, permanent=False):
        self.send_status(status_code=301 if permanent else 302)
        self.set_headers({
            'Location': url,
        })

    def parse_request(self):
        raw_req = self.get_raw_request()
        if not raw_req:
            return

        try:
            head, body = raw_req.split(2 * SEPARATOR, 1)
        except ValueError:
            head, body = raw_req, None

        try:
            first_line, raw_headers = head.split(SEPARATOR, 1)
            method, route, protocol = first_line.split(' ')
            headers = {i.split(': ', 1)[0]: i.split(': ', 1)[1]
                       for i in raw_headers.split(SEPARATOR)}
        except ValueError:
            return

        return {
            'headers': headers,
            'method': method,
            'route': route,
            'http_protocol_version': protocol[-3:],
            'body': body,
        }

    def handle(self):
        req = self.parse_request()
        if req is None:
            return self.response('')
        route = req['route']
        method = req['method']

        logging.info(f'{req["method"]} {route}')

        # print(self.handlers)
        handle_class = user_handlers.get(route)
        if not handle_class or not callable(handle_class):
            return self.send_error_404()

        _handler = handle_class(self.request, req)
        handle_func = getattr(_handler, method.lower())
        if not handle_func:
            return self.send_error_405()
        handle_func()


class UserBaseHandler():

    def __init__(self, request, request_info):
        self.request = request
        self.request_info = request_info

    def send(self, data):
        self.request.send(data if isinstance(data, bytes) else data.encode())

    def set_headers(self, headers):
        self.send_separator()
        self.send(SEPARATOR.join('{}: {}'.format(k, v) for k, v in headers.items()))

    def send_status(self, status_code=200, http_protocol_version=None):
        http_protocol_version = \
            http_protocol_version or '1.1'
        assert http_protocol_version in ['1.0', '1.1']
        _status_code = int(status_code)
        status_desc = {
            200: 'OK',
            301: 'Move Permanently',
            302: 'Found',
            404: 'Not Found',
            405: 'Method Not Allowed',
        }.get(_status_code, 'WTF?!')
        self.send(f'HTTP/{http_protocol_version} {_status_code} {status_desc}')

    def send_separator(self, count=1):
        self.send(count * SEPARATOR)

    def response(self, body):
        self.send_status()
        self.set_headers({
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': len(body),
            'Connection': 'close',
        })
        self.send_body(body)

    def send_body(self, body):
        self.send_separator(2)
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

    def send_error(self, status_code, body=''):
        assert int(status_code) > 399
        self.send_status(status_code=status_code)
        self.send_body('<html><center><h1>Not Found</h1></center></html>')

    def send_error_404(self):
        self.send_error(404, '<html><center><h1>Not Found</h1></center></html>')

    def send_error_405(self):
        self.send_error(405, '<html><center><h1>Method Not Allowed</h1></center></html>')

    def send_error_500(self):
        self.send_error(500, '<html><center><h1>Server Error</h1></center></html>')

    def redirect(self, url, permanent=False):
        self.send_status(status_code=301 if permanent else 302)
        self.set_headers({
            'Location': url,
        })


class AfterHandler(UserBaseHandler):
    def get(self):
        self.response('<html><body><h1>Hello, world!?</h1></html>')


class IndexHandler(UserBaseHandler):
    def get(self):
        self.redirect('http://localhost:20000/after')


user_handlers = {
    '': IndexHandler,
    '/': IndexHandler,
    '/after': AfterHandler,
}

# https://stackoverflow.com/a/21442489
if __name__ == '__main__':
    serv = TCPServer(('', 20000), BaseHandler)
    serv.serve_forever()
