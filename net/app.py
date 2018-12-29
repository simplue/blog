import logging
from framework.web_frame import BaseHandler, Appication


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
    Appication({
        '': IndexHandler,
        '/': IndexHandler,
        '/after': AfterHandler,
    }, DefaultHandler).listen()
