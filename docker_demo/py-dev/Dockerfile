FROM python:2.7-alpine
MAINTAINER zh <zh@simplue.cc>

RUN pip install --no-cache-dir -i https://pypi.mirrors.ustc.edu.cn/simple tornado

# 使用共享目录的方式，所以不需要拷贝文件了
# COPY ./app.py /app/app.py

WORKDIR /app

EXPOSE 8888

CMD ["python2", "app.py"]
