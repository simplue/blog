FROM mongo:2
MAINTAINER zh <zh@simplue.cc>

# COPY ./requirements.txt /data/requirements.txt
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
#     && apk --no-cache add g++ libffi-dev zlib-dev jpeg-dev libwebp-dev openjpeg-dev \
# 	&& pip install --no-cache-dir -i https://pypi.mirrors.ustc.edu.cn/simple \
# 		-r /data/requirements.txt
#     # && pip install --no-cache-dir -i https://pypi.mirrors.ustc.edu.cn/simple \
#     #     supervisor
#
# WORKDIR /data/prop_web
#
# EXPOSE 9900
EXPOSE 27017

# VOLUME ["/data/prop_web"]

CMD ["mongod", "--smallfiles"]
