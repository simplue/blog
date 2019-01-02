import os
import logging
from framework.web_frame import BaseHandler, Appication

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class DefaultHandler(BaseHandler):
    def get(self):
        self.try_file()


class AfterHandler(BaseHandler):
    def get(self):
        self.render('show_route.html', {
            'route': self.parsed_request["route"]
        })


class IndexHandler(BaseHandler):
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
        self.render('hello.html', {
            'todos': []
        })


if __name__ == '__main__':
    settings = {
        'debug': True,
        'STATIC_DIR': os.path.join(BASE_DIR, 'static'),
        'TEMPLATE_DIR': os.path.join(BASE_DIR, 'template'),
    }
    Appication([
        ('/', IndexHandler),
        ('/after', AfterHandler),
        ('.*', DefaultHandler),
    ], settings).listen()
