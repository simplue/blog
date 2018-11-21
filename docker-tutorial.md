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
//  -d 后台启动
//  -t 空白容器
//  -p 映射端口 host-port:docker-port，需要确host-port不被占用
//  --name 容器名 ubuntu:bionic 是镜像名，如果本地没有会自动到服务器下载，可以用上面的命令查看本地镜像
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

