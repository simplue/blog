# 安装docker-ce
```
// 删除旧版docker
sudo apt-get remove docker docker-engine docker.io

// 首先安装依赖
sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common

// 信任 Docker 的 GPG 公钥(根据你的发行版，下面的内容有所不同。)
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

// 对于 amd64 架构的计算机，添加软件仓库
sudo add-apt-repository \
   "deb [arch=amd64] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

// 最后安装
sudo apt-get update
sudo apt-get install docker-ce
```

参考链接
[官方](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
[清华大学](https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/)
[官方](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

# 添加用户到docker组，避免使用sudo [参考链接](https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user)
```
// 完成后重新开窗口
sudo groupadd docker
sudo usermod -aG docker $USER
```

# 镜像加速
https://www.docker-cn.com/registry-mirror


# 操作

```
// 罗列本地镜像
docker image ls
docker images

// 拉取镜像
docker pull python:3.6.7-alpine3.8
docker pull unbuntu:18.04

// 罗列容器
//  -a 显示全部，含未运行容器
docker container ls
docker ps

// 手动启动容器，启动后会得到一个容器ID，在输出的最后一行
//  -d, --detach `Run container in background and print container ID` 后台运行并输出容器ID
//  -t, --tty  `Allocate a pseudo-TTY` 分配伪终端
//  -p, --publish list `Publish a container's port(s) to the host` 映射端口 host-port:docker-port，需要确host-port不被占用
//  --name string `Assign a name to the container` 为容器指定一个名字
    ubuntu:bionic 是镜像名，如果本地没有会自动到服务器下载，可以用上面的命令查看本地镜像
// 如果启动失败，容器可能也已经创建，如果继续创建会有重名错误
docker run -d -t -p 8721:5000 --name docker-ubuntu-demo ubuntu:bionic

// 删除容器
//  -f 强制删除，即使在运行中
docker rm -f useless-container-name

// 恢复运行
docker start container-name

// 停止运行
docker stop container-name



```
sed 改镜像 https://mirrors.ustc.edu.cn/help/ubuntu.html#id7

apt 占用 https://www.linuxidc.com/Linux/2014-06/103437.htm

# Dockerfile 构建

## 一个基础镜像文件
```
# 基础镜像
FROM python:2.7-alpine

# 创建/维护者
MAINTAINER zh <zh@simplue.cc>

# 执行命令
RUN pip install --no-cache-dir -i https://pypi.mirrors.ustc.edu.cn/simple tornado

# 复制文件
COPY ./app.py /app/app.py

# 指定工作目录，没有会自动创建
WORKDIR /app

# 暴露端口
EXPOSE 8888

# 启动命令
CMD ["python2", "app.py"]
```

# 构建镜像
```
# 写好 Dockerfile 后，需要使用 `docker build` 构建镜像
#   -t 指定标签，格式：`NAME:TAG`
#   -f, --file string，指定 Dockerfile 路径，默认为 "./Dockerfile"
docker build . -t tornado:0.0.1

# 构建完成后启动
docker run -p -d 127.0.0.1:8701:8888 --name tornado-demo tornado:0.0.1

# 访问
$ curl 127.0.0.1:8701
Hello, world
```

# 开发
```
# 先将上面的 Dockerfile 的 COPY 去除，重新构建镜像
# 首次启动
docker run -i \
        -p 8701:8888 \
        --mount type=bind,source="${PWD}",target=/app \
        --name tornado-demo \
        tornado:0.0.1

# 挂掉以后重启
docker start -i tornado-demo
```

# Docker Compose
安装，参考: http://get.daocloud.io/
```
sudo su
curl -L https://get.daocloud.io/docker/compose/releases/download/1.23.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
exit
```

docker-compose.yml
```
version: '3'

services:
  tornado-demo:
    build: .
    ports:
      - "8701:8888"
    depends_on:
      - mongo-demo
    volumes:
      - .:/app

  mongo-demo:
    image: "mongo:3.4"
```

# 常用镜像
|镜像|链接|
|:--:|:--:|
|python|https://hub.docker.com/_/python/|
|ubuntu|https://hub.docker.com/_/ubuntu/|
|nginx|https://hub.docker.com/_/nginx/|
|mariadb|https://hub.docker.com/_/mariadb/|
|phpmyadmin|https://hub.docker.com/r/phpmyadmin/phpmyadmin/|
|mysql|https://hub.docker.com/_/mysql/|
|redis|https://hub.docker.com/_/redis/|
|mongo|https://hub.docker.com/_/mongo/|
|ipython|https://hub.docker.com/r/jupyter/|
|node|https://hub.docker.com/_/node/|
|openresty|https://hub.docker.com/r/openresty/openresty/|
|gogs|https://hub.docker.com/r/gogs/gogs/|
|sentry|https://hub.docker.com/_/sentry/|
|drone|https://hub.docker.com/r/drone/drone/|

