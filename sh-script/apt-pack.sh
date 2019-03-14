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
				libffi-dev \
				build-essential \
				libmysqlclient-dev \
				python3-dev \
				python3-pip \
				python-dev \
				python-pip \
				zsh \
	&& mkdir -p $pip_folder \
	&& echo "[global]
timeout = 20
index-url = https://mirrors.aliyun.com/pypi/simple/

[install]
extra-index-url = https://mirrors.ustc.edu.cn/pypi/web/simple/
    https://pypi.doubanio.com/simple/" > $pip_conf_file \
	&& pip3 install --user -U pipenv \
	&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - \
	&& sudo add-apt-repository \
		"deb [arch=amd64] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu \
		$(lsb_release -cs) \
		stable" \
	&& sudo apt update \
	&& sudo apt -y install docker-ce \
	&& curl -L https://get.daocloud.io/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m) > /tmp/docker-compose \
	&& sudo cp /tmp/docker-compose /usr/local/bin/docker-compose \
	&& sudo chmod +x /usr/local/bin/docker-compose \
	&& sudo echo "{
    "registry-mirrors": ["https://registry.docker-cn.com"]
}" > /etc/docker/daemon.json \
	&& sudo usermod -aG docker $USER \
	&& sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" \
	&& git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
	&& echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc \
	&& source ./zsh-syntax-highlighting/zsh-syntax-highlighting.zsh \
	&& git config --add oh-my-zsh.hide-status 1 \
	&& git config --add oh-my-zsh.hide-dirty 1 \
    && sudo sudo passwd ubuntu
	

	