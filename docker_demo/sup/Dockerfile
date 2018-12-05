FROM python:2.7.15-alpine3.7
MAINTAINER zh <zh@simplue.cc>

# COPY ./requirements.txt /data/requirements.txt
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk --no-cache add supervisor

# WORKDIR /data/prop_web

# VOLUME ["/data/prop_web"]

CMD ["supervisord", "-c", "/etc/supervisord.conf"]
