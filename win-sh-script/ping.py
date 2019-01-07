# coding: utf-8
from __future__ import print_function

import os
import re
import time
import json
import signal
import datetime
import subprocess
import multiprocessing as mp

# PING_FILE_BASE_DIR = os.path.join(os.path.expanduser('~'), 'ping')
PING_FILE_BASE_DIR = os.path.join('.', 'ping')
if not os.path.isdir(PING_FILE_BASE_DIR):
    os.mkdir(PING_FILE_BASE_DIR)

gbk_to_utf8 = lambda s: s.decode('gbk').encode('utf-8').strip()

def path_of_ping_file(name):
    return os.path.join(PING_FILE_BASE_DIR, name)


def path_of_ping_json():
    return path_of_ping_file('ping.json')


def path_of_ping_raw(name):
    return path_of_ping_file('{}.txt'.format(name))


def write_ping_info():
    with open('hosts.json', 'r') as f:
        hosts = json.loads(f.read())

    all_names = [i.get('name') or i['host'] for i in hosts]
    data = []

    for index, name in enumerate(all_names):
        try:
            with open(path_of_ping_raw(name), 'r') as f:
                lines = f.readlines()
            if not lines or len(lines) < 2:
                data[name] = {
                    'url': hosts[index].get('url'),
                    'unable': True,
                }
                continue

            try:
                r = re.match(r'最短 = (\d+)ms，最长 = (\d+)ms，平均 = (\d+)ms', gbk_to_utf8(lines[-1]))
                if r is None:
                    return None
                _min, _max, _avg = [int(i) for i in r.groups()]
                r = re.match(r'数据包: 已发送 = (\d+)，已接收 = (\d+)，丢失 = (\d+) \((\d+)% 丢失\)，', gbk_to_utf8(lines[-3]))
                _, _, _, _loss = r.groups()
                _loss = int(float(_loss))
            except:
                _min = _avg = _max = 9999
                _loss = 100

            data.append({
                'host': hosts[index]['host'],
                'avg': _avg,
                'loss': _loss,
                # 'url': hosts[index].get('url') or hosts[index]['host'],
                # 'unable': _loss >= 80,
                # 'slow': (_avg >= 300) if _avg else None,
                # 'middle': (100 < _avg < 300) if _avg else None,
                # 'fast': (_avg <= 100) if _avg else None,
            })
        except IOError:
            pass

    data.sort(key=lambda i: i['avg'])
    with open(path_of_ping_json(), 'w') as f:
        output = json.dumps(data)
        f.write(output)
    print(json.dumps(data, indent=2))


def _ping(ip, name, cnt=None, timeout=None):
    _cnt = cnt or 10
    _timeout = timeout or 300
    # interval = 1

    ping_cmd = 'ping -n {} -w {} {}'.format(_cnt, _timeout, ip)
    with open(path_of_ping_raw(name), 'w') as f:
        subprocess.call(ping_cmd, stdout=f, shell=True)


FOO = True


def multicore():
    global FOO
    while FOO:
        with open('hosts.json', 'r') as f:
            hosts = json.loads(f.read())

        pool_args = [
            (i['host'],
             i.get('name') or i['host'],
             i.get('ping_count')) for i in hosts]
        pool_size = len(pool_args)
        rs = []

        pool = mp.Pool(pool_size)

        for item in pool_args:
            print('new ping [host: {}] at {}'.format(item[0], datetime.datetime.now()))
            r = pool.apply_async(_ping, item)
            rs.append(r)

        print('\n')
        pool.close()
        pool.join()

        for i in rs:
            i.get()

        write_ping_info()
        time.sleep(20)


if __name__ == '__main__':
    def exit(signum, frame):
        global FOO
        FOO = False


    signal.signal(signal.SIGINT, exit)
    signal.signal(signal.SIGTERM, exit)

    multicore()
