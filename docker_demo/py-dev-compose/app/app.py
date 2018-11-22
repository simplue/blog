# coding:utf-8

import pymongo
import tornado.web
import tornado.ioloop
import tornado.options
tornado.options.parse_command_line()

# 由 compose 提供 DNS 服务
# client = pymongo.MongoClient('mongodemo', 27017)
# db = client['tornado']
# collection = db['test']

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # exist = collection.find_one({'times': {'$gte': 0}})
        # if exist:
        #     collection.update({}, {'$inc': {'times': 1}})
        # else:
        #     collection.insert_one({'times': 2})
        #
        # exist = collection.find_one({'times': {'$gte': 0}})
        exist = {'times': '1'}
        self.finish("Hello, world {} times!".format(exist.get('times')))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
