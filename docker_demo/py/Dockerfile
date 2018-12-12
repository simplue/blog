FROM python:2.7-alpine

RUN pip install --no-cache-dir -i https://pypi.mirrors.ustc.edu.cn/simple tornado

COPY ./app.py /app/app.py

WORKDIR /app

EXPOSE 8888

CMD ["python2", "app.py"]
