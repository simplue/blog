#!/bin/bash

# 加引号就跪
pip_folder=~/.pip/
pip_conf_file=$pip_folder/pip.conf

# apt-help:
#	https://linux.die.net/man/8/apt-get
# package:
#	https://packages.ubuntu.com/
# python complie:
# 	https://stackoverflow.com/questions/27022373/python3-importerror-no-module-named-ctypes-when-using-value-from-module-mul
# mysql
# 	libmysqlclient-dev  => in 18.04 is default-libmysqlclient-dev
sudo apt update \
	&& sudo apt -y upgrade \
	&& sudo apt -y install \
			libssl-dev \
			openssl \
			python3-pip \
			python3-dev \
			python-pip \
			python-dev \
			libffi-dev \
			build-essential \
			libmysqlclient-dev \
	&& mkdir -p $pip_folder \
	&& echo "[global]
timeout = 20

index-url = https://mirrors.aliyun.com/pypi/simple/

[install]
extra-index-url = https://mirrors.ustc.edu.cn/pypi/web/simple/
				https://pypi.doubanio.com/simple/
				https://pypi.tuna.tsinghua.edu.cn/simple/" > $pip_conf_file \
	&& pip3 install --upgrade pip \
	&& pip3 install --user -U pipenv
	