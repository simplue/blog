# $PATH
单用户：

编辑 `~/.profile` 中的 `PATH=...`，然后 `source ~/.profile`
加入 ~/.*rc，如 `echo "source ~/.profile" >> ~/.zshrc` 使得每次启动都自动加载路径

所有用户：
```
nano /etc/environment
source /etc/environment
```

参考：
https://stackoverflow.com/a/32893983
https://superuser.com/questions/488173/how-can-i-edit-the-path-on-linux


# zsh
禁用 git 插件
共享大git仓库夹会导致卡顿，可禁用git插件，编辑主题文件，如 `~/.oh-my-zsh/themes/robyrussel.zsh-theme` 的 PROMPT 行
https://github.com/robbyrussell/oh-my-zsh/issues/3288

指令高亮
git clone https://github.com/zsh-users/zsh-syntax-highlighting


# python
编译安装 python 可能会遇到 `lsb_release` 指令执行失败的情况（例如可能此前替换了默认的 python，或其他原因），使用`sudo apt install lsb-release` 安装后，将
`lsb_release.py` 链接到 `site-packages` 中，如 `ln -s /usr/share/pyshared/lsb_release.py /usr/local/python/3.7.1/lib/python3.7/site-packages/lsb_release.py`
