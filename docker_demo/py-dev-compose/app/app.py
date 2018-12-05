# coding:utf-8

# import pymongo
import tornado.web
import tornado.ioloop
import tornado.options

tornado.options.parse_command_line()
import MySQLdb
import logging

# import pymysql
# import records
# # 由 compose 提供 DNS 服务
# # client = pymongo.MongoClient('mongodemo', 27017)
# # db = client['tornado']
# # collection = db['test']
# import os
# DB_CONNECT_STRING = 'mysql+mysqldb://root:{}@mysqldemo'.format(os.environ['MYSQL_ROOT_PASSWORD'])
# print(DB_CONNECT_STRING)
# db = records.Database(DB_CONNECT_STRING)
# connection = pymysql.connect(host='mysqldemo',
#                              user='root',
#                              password='ho',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

import os
db = MySQLdb.connect(
    host=os.getenv('MYSQL_HOST', 'localhost'),
    port=int(os.getenv('MYSQL_PORT', 3306)),
    user='root',
    passwd=os.getenv('MYSQL_ROOT_PASSWORD'),
)

# MYSQL_ROOT_PASSWORD=123456
# # MYSQL_USER=django
# # MYSQL_PASSWORD=secret
# MYSQL_DATABASE=myAppDB

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # rows = db.query('select * from active_users')  # or db.query_file('sqls/active-users.sql')
        # exist = collection.find_one({'times': {'$gte': 0}})
        # if exist:
        #     collection.update({}, {'$inc': {'times': 1}})
        # else:
        #     collection.insert_one({'times': 2})
        #
        # exist = collection.find_one({'times': {'$gte': 0}})
        # with conn.ge
        with db.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            DB_VERSION = cursor.fetchone()
            logging.info(DB_VERSION)
            # data = r.fetchone()
        # raise Exception
        # 使用execute方法执行SQL语句
        exist = {'times': '1'}
        logging.info('info')
        logging.error('error')
        logging.warning('warning')
        self.write('MYSQL VERSION: {}'.format(DB_VERSION))
        self.finish("Hello, world {} times!".format(exist.get('times')))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
