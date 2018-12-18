# ref: https://github.com/gliderlabs/docker-alpine/issues/181

FROM python:2.7.15-alpine3.7
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk add -q --no-cache --virtual .build-deps build-base mariadb-dev \
    && pip install -q --no-cache-dir mysqlclient \
    && apk add -q --no-cache mariadb-client-libs \
    && apk del .build-deps

# FROM python:2.7.15-alpine3.8
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
#     && apk add -q --no-cache --virtual .build-deps build-base mariadb-dev \
#     && pip install -q --no-cache-dir mysqlclient \
#     && apk add -q --no-cache mariadb-connector-c \
#     && apk del .build-deps
