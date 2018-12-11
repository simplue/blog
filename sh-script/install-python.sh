#!/bin/bash

# install complier
# 	https://askubuntu.com/questions/237576/no-acceptable-c-compiler-found-in-path
# check packages
#	https://askubuntu.com/questions/423355/how-do-i-check-if-a-package-is-installed-on-my-server
if [[ $(dpkg -l build-essential) == "" ]]; then
	echo "\"build-essential\" not found, u can install by \`sudo apt -y install build-essential\`"
	exit 1
fi

# check argument
# 	https://stackoverflow.com/questions/6482377/check-existence-of-input-argument-in-a-bash-shell-script
if [ -z "$1" ]; then
    echo "not version specify."
	exit 1
fi

version=$1
index_url="https://npm.taobao.org/mirrors/python"
file_name="Python-$version.tgz"
download_url="$index_url/$version/$file_name"
operate_folder="/tmp"
save_path="$operate_folder/$file_name"
extra_path="$operate_folder/Python-$version"
configure_prefix="/usr/local/python/$version"

# re & endswith: 
#	https://codingstandards.iteye.com/blog/1187353
#	https://stackoverflow.com/questions/21112707/check-if-a-string-matches-a-regex-in-bash-script
# get curl status code: 
#	https://superuser.com/questions/272265/getting-curl-to-output-http-status-code
#   https://stackoverflow.com/questions/38905489/how-to-check-if-the-curl-was-successful-and-print-a-message
#	status_code=$(curl -s -o /dev/null -I -w "%{http_code}" $index_url)
resp=$(curl --silent --max-time 15 --write-out "%{http_code}" $index_url)
if !([[ $resp =~ $version ]] && [[ $resp == *200 ]]); then
   # echo $resp
   echo "version: $version not found in: \"$index_url\""
   exit 1
fi

# promt
#	https://stackoverflow.com/questions/1885525/how-do-i-prompt-a-user-for-confirmation-in-bash-script
# case
# 	https://www.shellscript.sh/case.html
echo "version: $version founded"
read -p "Are you sure to download? y/Y to continue" -n 1 -r
echo    # (optional) move to a new line
if !([[ $REPLY =~ ^[Yy]$ ]]); then
    exit 0
fi

# test file exists
# 	https://stackoverflow.com/questions/40082346/how-to-check-if-a-file-exists-in-a-shell-script
if [ -e $save_path ]; then
    echo "file exitst"
else
    echo "dowloading..."
	wget -O $save_path $download_url
	echo "download complete"
fi


echo "extracting..."
tar -xzvf $save_path --directory $operate_folder
echo "extract complete"

cd $extra_path && ./configure --prefix=$configure_prefix && make && sudo make install && sudo rm -rf $extra_path

exit 0
