# -*- coding: utf-8 -*-

import os
import redis
import pymongo
import MySQLdb
import datetime
import tornado.web
import tornado.gen
import tornado.ioloop
import tornado.options

tornado.options.parse_command_line()

try:
    mongo = pymongo.MongoClient(
        host=os.getenv('MONGO_HOST', 'localhost'),
        port=int(os.getenv('MONGO_PORT', 27017)),
    )
except:
    mongo = None

try:
    red = redis.Redis(
        host=os.getenv('REDIS_HOST', 'localhost'),
        port=int(os.getenv('REDIS_PORT', 6379)),
    )
except:
    red = None

try:
    mysql = MySQLdb.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        port=int(os.getenv('MYSQL_PORT', 3306)),
        user='root',
        passwd=os.getenv('MYSQL_ROOT_PASSWORD'),
        db=os.getenv('MYSQL_DATABASE'),
    )
except:
    mysql = None


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<h1 style="color: #aaa">Hello now: {}</h1>'.format(datetime.datetime.now()))

        if mysql:
            with mysql.cursor() as cursor:
                cursor.execute("SELECT VERSION()")
                _VERSION = cursor.fetchone()

            self.write('<h1>MYSQL VERSION: {}</h1>'.format(_VERSION[0]))
        else:
            self.write('<h1>MYSQL MISS</h1>')

        if mongo:
            self.write('<h1>MONGO VERSION: {}</h1>'.format(mongo.server_info().get('version')))
        else:
            self.write('<h1>MONGO MISS</h1>')

        if red:
            self.write('<h1>REDIS VERSION: {}</h1>'.format(red.info().get('redis_version')))
        else:
            self.write('<h1>REDIS MISS</h1>')


@tornado.gen.coroutine
def do_something(func_name):
    print 'from {} invoke at {}'.format(func_name, datetime.datetime.now())


@tornado.gen.coroutine
def minute_loop():
    while True:
        sleep = tornado.gen.sleep(60)
        yield do_something(minute_loop.__name__)
        yield sleep


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)


if __name__ == "__main__":
    make_app().listen(8888)
    event_loop = tornado.ioloop.IOLoop.current()
    event_loop.spawn_callback(minute_loop)
    event_loop.start()
'''
docker run -d --name=netdata \
  -p 19999:19999 \
  -v /proc:/host/proc:ro \
  -v /sys:/host/sys:ro \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -e PGID=999 \
  --cap-add SYS_PTRACE \
  --security-opt apparmor=unconfined \
  netdata/netdata
'''