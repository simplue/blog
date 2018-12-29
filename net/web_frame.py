import re
import os
import json
import time
import socket
import logging
import traceback
from functools import wraps
from template_engine import Templite, remove_all_blank, remove_all_blank_n_split, join_n_remove_all_blank
from socketserver import BaseRequestHandler, ThreadingTCPServer

SEPARATOR = '\r\n'
MAX_PACKET = 1024

FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel('INFO'.upper())

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'template')

fuck_error = lambda: logging.error(traceback.format_exc())


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


STATUS_CODE_DESC = {
    200: 'OK',
    301: 'Move Permanently',
    302: 'Found',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    500: 'Internal Server Error',
}
get_desc_by_status_code = lambda code: STATUS_CODE_DESC.get(code, 'WTF?!')

to_bytes = lambda _str: _str.encode('utf-8')
to_str = lambda _bytes, charset=None: _bytes.decode(charset or 'utf-8')
_s = to_utf8 = to_str
_b = to_bytes
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
                chunk = self.request.recv(MAX_PACKET).strip()
                req_data.append(chunk)
            except socket.timeout:
                return b''.join(req_data)

    def parse_body(self, body, header_info):
        if not body:
            return {}, {}

        raw_content_type = header_info['headers'].get('content-type')
        charset = 'utf-8'
        content_type = raw_content_type
        if 'charset' in raw_content_type:
            try:
                content_type, charset = raw_content_type.split(';')[-1].split('=')[-1]
            except ValueError:
                pass

        boundary_match = re.match(r'multipart/form-data;.*boundary=([\-\w]+);?', raw_content_type)
        boundary = boundary_match.group(1) if boundary_match else None

        parsed_body = parsed_files = None
        if content_type == 'application/x-www-form-urlencoded':
            parsed_body = {}
            _body = _s(body, charset)
            pairs = remove_all_blank_n_split(_body, '&')
            for pair in pairs:
                if not pair:
                    continue
                key, value = remove_all_blank_n_split(pair, '=')
                parsed_body[key] = value

        elif content_type.startswith('multipart/form-data'):
            if not boundary:
                return
            # logging.info('\n=================\n\n%s\n\n=================\n' % (body, ))
            parsed_body = {}
            parsed_files = {}
            chunks = body.split(b'--' + _b(boundary))
            for chunk in chunks:
                if chunk in [b'--', b'']:
                    continue

                _form_key = _file_name = _file_content_type = None
                chunk_lines = chunk.split(_b(SEPARATOR))
                for line in chunk_lines:
                    if not line:
                        continue

                    if not _form_key and not _file_name:
                        value_match = re.match(
                            b'^Content-Disposition:\s*form-data;\s*name="([_\w]+)";?$', line)

                        if value_match:
                            _form_key = value_match.group(1)
                            break

                        file_match = re.match(
                            b'^Content-Disposition:\s*form-data;\s*name="([_\w]+)";\s*filename="([_\.\w]+);?"$', line)

                        if file_match:
                            _form_key, _file_name = file_match.group(1), file_match.group(2)
                            continue

                    if _file_name and not _file_content_type:
                        content_type_match = re.match(
                            b'^Content-Type:\s*([\_/\w]+)', line)
                        if content_type_match:
                            _file_content_type = content_type_match.group(1)
                        break

                content = chunk_lines[-2]
                if _file_name:
                    parsed_files[_s(_form_key)] = {
                        'file_name': _s(_file_name) if _file_name is not None else None,
                        'content_type': _s(_file_content_type) if _file_content_type is not None else None,
                        'content': content,
                    }
                elif _form_key:
                    parsed_body[_s(_form_key)] = _s(content)

        elif content_type == 'application/json':
            parsed_body = json.loads(_s(body), encoding=charset)
            if isinstance(parsed_body, list):
                return

        return parsed_body, parsed_files

    def parse_header(self, head):
        try:
            _head = head if isinstance(head, str) else _s(head)
            first_line, raw_headers = _head.split(SEPARATOR, 1)
            method, route, protocol = first_line.split()

            query = {}
            if '?' in route:
                route, query_str = route.split('?', 1)
                pairs = remove_all_blank_n_split(query_str, '&')
                for pair in pairs:
                    if not pair:
                        continue
                    key, value = remove_all_blank_n_split(pair, '=')
                    query[key] = value

            headers = {}
            for header_line in raw_headers.split(SEPARATOR):
                head_name, content = remove_all_blank_n_split(header_line, ':', 1)
                headers[head_name.lower()] = content

            return {
                'query': query,
                'headers': headers,
                'method': method,
                'route': (route[:-1] if route.endswith('/') else route) or '/',
                'http_protocol_version': protocol[-3:],
            }
        except ValueError:
            pass

    def parse_request(self):
        raw_req = self.get_raw_request()
        if not raw_req:
            return

        try:
            head, body = raw_req.split(2 * _b(SEPARATOR), 1)
        except ValueError:
            head, body = raw_req, None

        header_info = self.parse_header(head)
        if header_info is None:
            return 400

        req_method = header_info['method'].lower()
        if req_method not in ['get', 'post']:
            return 405

        if req_method == 'post':
            parsed_body = self.parse_body(body, header_info)
            if parsed_body is None:
                return 400
            header_info['body'], header_info['files'] = parsed_body

        return header_info

    def pong(self, status_code):
        self.request.send(_b(f'HTTP/1.0 {status_code} {get_desc_by_status_code(status_code)}{SEPARATOR}Connection: close{2 * SEPARATOR}'))

    @timming
    def handle(self):
        try:
            parsed_request = self.parse_request()
        except:
            fuck_error()
            return self.pong(500)

        if parsed_request is None:
            return self.pong(200)
        elif isinstance(parsed_request, int):
            return self.pong(parsed_request)

        route, method = parsed_request['route'], parsed_request['method']
        handle_class = user_handlers.get(route) or DefaultHandler
        handler = handle_class(self.request, parsed_request)

        handle_func = handler.get if handle_class is DefaultHandler \
            else getattr(handler, method.lower())
        try:
            handle_func()
        except:
            handler.send_error(500, traceback.format_exc())

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

        _status_code = self.__status_code
        self.write_head_buffer(''.join([
            f'HTTP/{http_protocol_version} {_status_code} {get_desc_by_status_code(_status_code)}',
            SEPARATOR,
            SEPARATOR.join('{}: {}'.format(k, v) for k, v in self.__headers.items()),
            2 * SEPARATOR,
        ]))
        self.__finished = True

    def send_all(self):
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
        self.render(template_path, {'request': self.parsed_request})

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
        self.render('show_route.html', {
            'route': self.parsed_request["route"]
        })


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

    def post(self):
        logging.info(self.parsed_request['query'])
        logging.info(self.parsed_request.get('body'))
        logging.info(self.parsed_request.get('files'))
        self.render('show_route.html', {
            'route': self.parsed_request["route"]
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
