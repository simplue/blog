import os
import time
import socket
import logging
from functools import wraps
from template_engine import Templite
from socketserver import BaseRequestHandler, ThreadingTCPServer

SEPARATOR = '\r\n'
MAX_PACKET = 1024

FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel('INFO'.upper())

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'template')


def timming(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        try:
            req, resp = func(*args, **kwargs)
        except TypeError:
            return

        logging.info(f'{resp["status_code"]} {req["method"]} {req["route"]} {int((time.time() - start) * 1000)}ms')
        return req

    return inner


# byte:
#   https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
# server-demo:
#   https://stackoverflow.com/a/10114266
# shutdown server:
#   https://stackoverflow.com/a/21442489
# socket reuse:
#   https://stackoverflow.com/q/17659334
class BaseHandler(BaseRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handlers = user_handlers

    def get_raw_request(self):
        self.request.settimeout(0.001)
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

    def pong(self):
        self.request.send(f'HTTP/1.0 200 OK{SEPARATOR}Connection: close{2 * SEPARATOR}'.encode())

    @timming
    def handle(self):
        parsed_request = self.parse_request()
        if parsed_request is None:
            return self.pong()

        route, method = parsed_request['route'], parsed_request['method']
        handle_class = user_handlers.get(route) or DefaultHandler
        handler = handle_class(self.request, parsed_request)

        handle_func = handler.get if handle_class is DefaultHandler \
            else getattr(handler, method.lower())
        try:
            handle_func()
        except:
            import traceback
            handler.send_error_500(traceback.format_exc())

        if not handler.is_finished():
            handler.finish()
        handler.send_all()

        return parsed_request, handler.get_resp_info()


def no_write_after_finish(func):
    @wraps(func)
    def inner(handler, *args, **kwargs):
        if handler.is_finished():
            raise Exception('can not write after finished')
        return func(handler, *args, **kwargs)

    return inner


class UserBaseHandler():

    def __init__(self, request, parsed_request):
        self.request = request
        self.parsed_request = parsed_request
        self.__buffer = []
        self.__head_buffer = []
        self.__headers = {}
        self.__status_set = False
        self.__status_code = 200
        self.__finished = False
        self.__http_status_error = False
        self.__default_http_protocol_version = '1.1'

    @no_write_after_finish
    def write(self, chunk):
        if self.__finished:
            raise Exception('request has been finish')

        if not chunk:
            raise Exception('chunk can not be empty')

        self.__buffer.append(chunk if isinstance(chunk, bytes) else chunk.encode())

    @no_write_after_finish
    def write_head_buffer(self, chunk):
        if self.__finished:
            raise Exception('request has been finish')

        if not chunk:
            raise Exception('chunk can not be empty')

        self.__head_buffer.append(chunk if isinstance(chunk, bytes) else chunk.encode())

    def clean_resp(self):
        self.__buffer = []
        self.__head_buffer = []
        self.__headers = {}
        self.__status_set = False
        self.__status_code = 200
        self.__finished = False

    def is_finished(self):
        return self.__finished

    def try_file(self):
        file_path = os.path.join(
            STATIC_DIR,
            self.parsed_request['route'][1:].replace('static/', ''))
        if not os.path.isfile(file_path):
            return self.send_error_404()

        with open(file_path, 'rb') as f:
            file_content = f.read()
            ext = file_path.split(".")[-1]
            self.set_headers(**{
                'Content-Type': f'image/{"webp" if ext == "ico" else ext}',
                'Content-Length': len(file_content),
            })
            self.finish(file_content)

    def finish(self, chunk=None):
        if self.__finished:
            raise Exception('request has been finish')

        if chunk:
            self.write(chunk)

        http_protocol_version = self.parsed_request['http_protocol_version'] \
                                or self.__default_http_protocol_version
        assert http_protocol_version in ['1.0', '1.1']
        status_desc = {
            200: 'OK',
            301: 'Move Permanently',
            302: 'Found',
            404: 'Not Found',
            405: 'Method Not Allowed',
            500: 'Internal Server Error',
        }.get(self.__status_code, 'WTF?!')

        self.write_head_buffer(''.join([
            f'HTTP/{http_protocol_version} {self.__status_code} {status_desc}',
            SEPARATOR,
            SEPARATOR.join('{}: {}'.format(k, v) for k, v in self.__headers.items()),
            2 * SEPARATOR,
        ]))
        self.__finished = True

    def send_all(self):
        print(self.__head_buffer)
        print(self.__buffer)
        self.request.send(b''.join(self.__head_buffer))
        self.request.send(b''.join(self.__buffer))

    @no_write_after_finish
    def set_headers(self, **headers):
        self.__headers.update(headers)

    @no_write_after_finish
    def set_status(self, status_code):
        if self.__status_set:
            raise Exception('headers has been set')
        self.__status_set = True
        self.__status_code = int(status_code)

    def get_resp_info(self):
        return {
            'status_code': self.__status_code
        }

    def text_response(self, body):
        self.set_status(200)
        self.set_headers(**{
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': len(body),
        })
        self.finish(body)

    def send_error(self, status_code, body=None, template_path=None):
        assert int(status_code) > 399
        self.__http_status_error = True
        self.clean_resp()
        self.set_status(status_code)
        if body:
            return self.finish(body)
        self.render(template_path)

    def send_error_404(self):
        self.send_error(404, template_path='404.html')

    def send_error_405(self):
        self.send_error(405, template_path='405.html')

    def send_error_500(self):
        self.send_error(500, template_path='500.html')

    def redirect(self, url, permanent=False):
        self.set_status(301 if permanent else 302)
        self.set_headers(Location=url)
        self.finish()

    def render(self, template_path, context=None):
        template_full_path = os.path.join(TEMPLATE_DIR, template_path)
        if not os.path.isfile(template_full_path):
            return self.send_error_404()

        with open(template_full_path, 'r') as f:
            content = Templite(f.read()).render(context)
            self.set_headers(**{
                'Content-Type': 'text/html; encoding=utf8',
                'Content-Length': len(content),
            })
            self.write(content)

    def get(self):
        self.send_error_405()

    def post(self):
        self.send_error_405()

    def put(self):
        self.send_error_405()

    def delete(self):
        self.send_error_405()

    def option(self):
        self.send_error_405()

    def head(self):
        self.send_error_405()


class DefaultHandler(UserBaseHandler):
    def get(self):
        self.try_file()


class AfterHandler(UserBaseHandler):
    def get(self):
        context = {
            'show_route': self.parsed_request["route"]
        }
        self.render('hello.html', context)


class IndexHandler(UserBaseHandler):
    def get(self):
        self.render('hello.html', {
            'todos': [
                {
                    'name': 'ho',
                    'time': '2017-10-10',
                    'content': '吃饭',
                },
                {
                    'name': 'ho',
                    'time': '2017-10-10',
                    'content': '睡觉',
                },
                {
                    'name': 'ho',
                    'time': '2017-10-10',
                    'content': '打豆豆',
                },
            ]
        })


user_handlers = {
    '': IndexHandler,
    '/': IndexHandler,
    '/after': AfterHandler,
}

if __name__ == '__main__':
    server = ThreadingTCPServer(('', 20000), BaseHandler, False)
    server.allow_reuse_address = True
    server.server_bind()
    server.server_activate()
    try:
        server.serve_forever()
    except:
        server.shutdown()
