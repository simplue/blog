FROM python:2.7.15-alpine3.7

COPY ./requirements.txt /tmp/requirements.txt

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk add --no-cache g++ libffi-dev zlib-dev jpeg-dev libwebp-dev openjpeg-dev libxml2-dev libxslt-dev \
    && mkdir -p ~/.pip \
    && printf "[global]\ntimeout = 30\nindex-url = https://mirrors.aliyun.com/pypi/simple/\n" > ~/.pip/pip.conf \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -f /tmp/requirements.txt
