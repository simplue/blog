FROM python:2.7.15-alpine3.7
MAINTAINER zh <zh@simplue.cc>

COPY ./requirements.txt /tmp/requirements.txt

# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.huaweicloud.com/g' /etc/apk/repositories

# VER 1 ref: https://github.com/gliderlabs/docker-alpine/issues/181
RUN apk add --no-cache --virtual .build-deps build-base mariadb-dev \
    && pip install --no-cache-dir -i https://pypi.mirrors.ustc.edu.cn/simple -r /tmp/requirements.txt \
    && apk del .build-deps \
    && apk add --no-cache mariadb-client-libs

RUN apk -q --no-cache add mariadb-client-libs

EXPOSE 8888

WORKDIR /app

# CMD ["python2", "app.py"]
