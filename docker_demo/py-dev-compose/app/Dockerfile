FROM python:2.7.15-alpine3.7
MAINTAINER zh <zh@simplue.cc>

COPY ./requirements.txt /tmp/requirements.txt

# ref: https://github.com/gliderlabs/docker-alpine/issues/181
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk add -q --no-cache --virtual .build-deps build-base mariadb-dev \
    && pip install -q --no-cache-dir -r /tmp/requirements.txt \
    && apk add -q --no-cache mariadb-client-libs \
    && apk del .build-deps \
    && rm -f /tmp/requirements.txt

WORKDIR /app
