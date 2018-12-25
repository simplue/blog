import re
import os
import time
import subprocess
import tornado.ioloop
import tornado.autoreload

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_FILE = os.path.join(BASE_DIR , 'web_frame.py')

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
    # subprocess.Popen(f'pipenv run python {SERVER_FILE}')
    subprocess.Popen(['pipenv', 'run', 'python', SERVER_FILE])
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


# https://stackoverflow.com/a/21442489
if __name__ == '__main__':
    reload_server()
    tornado.autoreload.start(check_time=500)
    tornado.autoreload.watch(SERVER_FILE)
    tornado.ioloop.IOLoop.instance().start()
