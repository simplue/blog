# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.options
tornado.options.parse_command_line()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish("Hello, world!1!")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
