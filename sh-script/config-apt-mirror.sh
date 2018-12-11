#!/bin/bash

current_mirror_list="/etc/apt/sources.list"
raw_mirror_list="/etc/apt/raw.sources.list"
aliyun_mirror_list="/etc/apt/aliyun.sources.list"
ustc_mirror_list="/etc/apt/ustc.sources.list"

if !([ -e $raw_mirror_list ]); then 
	sudo cp $current_mirror_list $raw_mirror_list
	echo "backup raw source list"
fi

if !([ -e $aliyun_mirror_list ]); then
	echo "deb https://mirrors.aliyun.com/ubuntu/ xenial main
	# deb-src https://mirrors.aliyun.com/ubuntu/ xenial main
	deb https://mirrors.aliyun.com/ubuntu/ xenial-updates main
	# deb-src https://mirrors.aliyun.com/ubuntu/ xenial-updates main
	deb https://mirrors.aliyun.com/ubuntu/ xenial universe
	# deb-src https://mirrors.aliyun.com/ubuntu/ xenial universe
	deb https://mirrors.aliyun.com/ubuntu/ xenial-updates universe
	# deb-src https://mirrors.aliyun.com/ubuntu/ xenial-updates universe
	deb https://mirrors.aliyun.com/ubuntu/ xenial-security main
	# deb-src https://mirrors.aliyun.com/ubuntu/ xenial-security main
	deb https://mirrors.aliyun.com/ubuntu/ xenial-security universe
	# deb-src https://mirrors.aliyun.com/ubuntu/ xenial-security universe" | sudo tee $aliyun_mirror_list && cat $aliyun_mirror_list
fi

if !([ -e $ustc_mirror_list ]); then
	echo "deb https://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse
	# deb-src https://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse
	deb https://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
	# deb-src https://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
	deb https://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
	# deb-src https://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
	deb https://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
	# deb-src https://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse" | sudo tee $ustc_mirror_list && cat $ustc_mirror_list
fi

cat $current_mirror_list

read -p "swtich (ustc / ali|aliyun / raw)?" choice
case "$choice" in 
	ustc ) 
		target=$ustc_mirror_list
		;;
	ali|aliyun ) 
		target=$aliyun_mirror_list
		;;
	raw )
		target=$raw_mirror_list
		;;
	* ) 
		echo "not change"
		exit 0
		;;
esac

sudo cp $target $current_mirror_list
cat $current_mirror_list
echo "change to $target"

# apt update
read -p "apt update now? (y|Y to continue)" choice
case "$choice" in 
	y|Y ) 
		sudo apt update
		;;
	* ) 
		echo "no update"
		;;
esac
