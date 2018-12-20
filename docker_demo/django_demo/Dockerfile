FROM python:3.6-alpine3.7

COPY ./requirements.txt /tmp/requirements.txt

# mariadb-client for mysqldump
# mariadb-client-libs for run mysql driver
# jpeg-dev for pillow
# .build-deps for pip install mysql driver
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk add --no-cache --virtual .build-deps build-base mariadb-dev \
    && apk add --no-cache mariadb-client-libs mariadb-client jpeg-dev \
    && mkdir -p ~/.pip \
    && printf "[global]\ntimeout = 30\nindex-url = https://mirrors.aliyun.com/pypi/simple/\n" > ~/.pip/pip.conf \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && apk del .build-deps \
    && rm -f /tmp/requirements.txt
