#!/bin/bash

if [ -z "$1" ]; then
    echo "not version specify."
	exit 1
fi

version=$1
# substring:
# 	https://stackoverflow.com/questions/18864840/bash-substring-of-a-constant-string
python_bin="/usr/local/python/$version/bin/python$(expr substr $version 1 1)"
echo $python_bin

# pipenv --python $python_bin
if [ -e $python_bin ]; then 
	pipenv --python $python_bin
else
	echo "Python $version not install"
fi

sed -i 's/pypi.org\/simple/mirrors.aliyun.com\/pypi\/simple\//g' Pipfile

if [ -e "requirements.txt" ]; then 
	echo 'detect requirements.txt installing...'
	pipenv install -r requirements.txt
fi

cat Pipfile
pipenv run python -V

exit 0
