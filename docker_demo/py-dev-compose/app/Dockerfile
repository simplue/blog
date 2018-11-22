FROM python:2.7-alpine
MAINTAINER zh <zh@simplue.cc>

COPY ./requirement.txt /tmp/requirement.txt

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk --no-cache add bash
RUN pip install --no-cache-dir -i https://pypi.mirrors.ustc.edu.cn/simple -r /tmp/requirement.txt

EXPOSE 8888

WORKDIR /app

# CMD ["python2", "app.py"]
