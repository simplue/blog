

# Box 下载
https://app.vagrantup.com/

http://www.vagrantbox.es/

https://cloud-images.ubuntu.com/

https://mirrors.tuna.tsinghua.edu.cn/ubuntu-cloud-images/

https://mirrors.huaweicloud.com/ubuntu-cloud-images/

https://mirrors.ustc.edu.cn/ubuntu-cloud-images/

https://mirrors.nju.edu.cn/ubuntu-cloud-images/

在 app.vagrantup.com 中手动下载 box
```
(手动下载：https://stackoverflow.com/questions/28399324/download-vagrant-box-file-locally-from-atlas-and-configuring-it)

先进入一个版本页面，然后在链接后面补上 /providers/virtualbox.box 即可跳转到下载链接，页面顺序

=> https://app.vagrantup.com/ubuntu/boxes/trusty64

=> https://app.vagrantup.com/ubuntu/boxes/trusty64/versions/20181103.0.0

=> https://app.vagrantup.com/ubuntu/boxes/trusty64/versions/20181103.0.0/providers/virtualbox.box
```

# 磁盘扩容
## 使用插件
试验结果是配置后不再需要分区软件（但没有交换分区），不过建议还是要检查。

https://github.com/sprotheroe/vagrant-disksize

```
# 安装插件
vagrant plugin install vagrant-disksize

# 停机
vagrant halt

# 在 Vagrantfile 加入
config.disksize.size = '100GB'

# 开机
vagrant up
```

## 手动扩容
在 virtualbox 上找到磁盘路径，一般在 `C:\Users\username\VirtualBox VMs\`下。
```
# VBoxManage 命令在 virtualbox 安装目录下，一般是

# 复制当前挂载磁盘为 vdi 格式，vdi 才支持扩容
VBoxManage clonehd "xxx.vmdk" "xxx.vdi" --format vdi

# resize 单位默认是 MB，102400 等同 100G
VBoxManage modifyhd "clone-disk1.vdi" --resize 102400
```

在 virtualbox 上删除原来挂载的磁盘（先前的 vmdk 文件也可以删除了），将新的磁盘挂载上去。接着就是使用 gparted 分区了。

下载分区软件 gparted： https://gparted.org/download.php ，以默认选项进入界面，选中需要扩容的磁盘，点击菜单栏的`resize/move`拉满容量即可，最后应用配置就完成了。

参考：

比较详尽的教程：https://tvi.al/resize-sda1-disk-of-your-vagrant-virtualbox-vm/

gparted 配置交换分区：https://askubuntu.com/questions/180730/how-do-i-restore-a-swap-partition-i-accidentally-deleted

全手动（不过试验失败了）：https://gist.github.com/christopher-hopper/9755310

# 可用插件列表
https://github.com/hashicorp/vagrant/wiki/Available-Vagrant-Plugins

