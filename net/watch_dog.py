import re
import os
import time
import subprocess
from tornado import ioloop
from tornado import autoreload

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
get_file_path = lambda file_name: os.path.join(BASE_DIR, file_name)
APP_FILE = get_file_path('app.py')


def get_pid():
    time.sleep(1)
    # cmd = 'netstat -aonp TCP'
    cmd = 'sudo netstat -ltpn'
    porc = subprocess.Popen(cmd, shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    output = porc.communicate()[0]
    # for line in output.decode('gbk').split('\r\n'):
    for line in output.decode().split('\n'):
        # r = re.match(r'.+0.0.0.0:20000.+0.0.0.0:0.+LISTENING(\s+)(\d+)', line)
        r = re.match(r'.+0.0.0.0:20000.+LISTEN(\s+)(\d+).+', line)
        if r:
            return r.group(2)


def start_server():
    subprocess.Popen(['pipenv', 'run', 'python', APP_FILE])
    new_server_pid = get_pid()
    limit = 5
    while not new_server_pid:
        new_server_pid = get_pid()
        limit -= 1
        if limit < 0:
            print(f'RELOAD SERVER OVER 5 TIMES')
            return

    print(f'NEW SERVER UP RUN AT PID: {new_server_pid}')
    return new_server_pid


def reload_server():
    pid = get_pid()
    if pid:
        print('GO TO KILL SERVER_PID ==', pid)
        # os.system(f'taskkill /F /PID {pid}')
        subprocess.Popen(['sudo', 'kill', '-9', pid])
        old_server_pid = get_pid()
        while old_server_pid:
            old_server_pid = get_pid()
        print('OLD SERVER KILLED')

    while not start_server():
        pass


def get_watch_files():
    this_file_abspath = os.path.abspath(__file__)
    all_watch_files = []

    for dir, _, files in os.walk('.'):
        for file in files:
            _file_abspath = os.path.abspath(os.path.join(dir, file))

            if not _file_abspath.endswith('.py') \
                or file.endswith('__init__.py') \
                or this_file_abspath == _file_abspath:
                continue

            all_watch_files.append(_file_abspath)

    return all_watch_files


# https://stackoverflow.com/a/16974952
def files_auto_reload():
    autoreload.start(check_time=500)
    for file in get_watch_files():
        autoreload.watch(file)


# https://stackoverflow.com/a/21442489
if __name__ == '__main__':
    files_auto_reload()
    reload_server()
    ioloop.IOLoop.instance().start()
