## ls
`ls`是[list](https://dictionary.cambridge.org/us/dictionary/english-chinese-simplified/list)(罗列)的缩写, 用于罗列指定目录下的文件及目录.
```
# 当前目录
$ ls
foo1  foo2  foo3
# 指定目录
$ ls ~/Desktop/test
foo1  foo2  foo3
# -a 显示(即以"."开头的)隐藏文件及目录
$ ls -a
.  ..  foo1  foo2  foo3
# -l显示详细信息, 第一行为整个目录占用的空间, 接下来的信息从左至右依次为:
# 权限:
#     bit 0: 文件类型:
#         '-': 普通文件
#         'd(directory)': 文件夹
#         's(sock)': sock文件
#         'l(link)': 软链接
#         'b(block)': 设备文件, 通常在/dev下
#         'p(pipe)': 命令管道文件
#         'c(character)': 字符设备文件(如键盘、字符终端等), 通常在/dev下
#     bit 1~3: 所属者权限
#     bit 4~6: 所属组权限
#     bit 7~9: 其他用户权限
#     3种权限: 'r(read)': 读; 'w(write)': 写, 'x(execute)': 执行
# 硬链接数
# 所属者
# 所属组
# 文件大小(默认单位: 字节)
# 最后变更时间
# 文件/目录名
$ ls -al
total 20
drwxrwxr-x 2 ho ho 4096 Oct 12 08:58 .
drwxr-xr-x 4 ho ho 4096 Oct 12 07:51 ..
-rw-rw-r-- 1 ho ho   15 Oct 12 08:33 foo1
-rw-rw-r-- 1 ho ho   15 Oct 12 08:30 foo2
-rw-rw-r-- 1 ho ho   15 Oct 12 08:30 foo3
# -h 给人看的(humance), 主要区别在文件容量单位变得更好理解
$ ls -alh
total 20K
drwxrwxr-x 2 ho ho 4.0K Oct 12 08:58 .
drwxr-xr-x 4 ho ho 4.0K Oct 12 07:51 ..
-rw-rw-r-- 1 ho ho   15 Oct 12 08:33 foo1
-rw-rw-r-- 1 ho ho   15 Oct 12 08:30 foo2
-rw-rw-r-- 1 ho ho   15 Oct 12 08:30 foo3
```

## cat
`cat`是[concatenate](https://dictionary.cambridge.org/us/dictionary/english-chinese-simplified/concatenate)(使连接)的缩写, 最常见的用法是查看文件的内容, 同时也可以用于创建文件和连接文件等

```
# 查看单个文件(文件内容是文件名+换行符)
$ cat foo1
This is foo1.

# -e 在行末和结尾处带上'$'符号
$ cat -e foo1
This is foo1.$
$
# -n 展示行号
$ cat -n foo1
     1	This is foo1.
     2

# 查看多个文件(连接多个文件并输出)
$ cat -en foo1 foo2 foo3
     1	This is foo1.$
     2	$
     3	This is foo2.$
     4	$
     5	This is foo3.$
     6	$

# 检索文件中某个关键字, 并输出关键字所在行和该行上下N行的内容(这里关键字是ERROR, N是2)
$ cat -en fooLog | grep ERROR -2
     8	...$
     9	...$
    10	ERROR ONE!$
    11	...$
    15	...$
--
    24	...$
    25	...$
    26	ERROR TWO!$
    27	...$
    31	...$

# 创建文件
# 输入命令后, 系统会等待用户输入, 完成输入以后, 按"Ctr+D"完成, 对于已存在的文件, ">"会覆盖原内容, 追加内容要用">>"
$ cat > newFoo
This is newFoo.

$ cat -en newFoo
     1	This is newFoo.$
     2	$

# 复制创建
$ cat foo1 > foo1Copy
$ cat -en foo1Copy
     1	This is foo1.$
     2	$

# 连接foo1, foo2, foo3的内容, 然后输出到mixFoo中
$ cat foo1 foo2 foo3 > mixFoo
$ cat -en mixFoo
     1	This is foo1.$
     2	$
     3	This is foo2.$
     4	$
     5	This is foo3.$
     6	$

# 连接foo1, foo2, foo3的内容并排序(按行), 然后输出到mixFooSorted中
$ cat foo1 foo2 foo3 | sort > mixFooSorted
$ cat -en mixFooSorted
     1	$
     2	$
     3	$
     4	This is foo1.$
     5	This is foo2.$
     6	This is foo3.$
```

## mv
`mv`是[move](https://dictionary.cambridge.org/us/dictionary/english-chinese-simplified/move)(移动)的缩写, 用于移动或重命名文件或目录.
```
# 移动
mv foo1 ~/Desktop/

# 重命名
$ ls
foo2  foo3
$ mv foo2 foo1
$ ls
foo1  foo3

# 可以将要删除的文件移动至/tmp目录, 默认情况下/tmp目录下的文件重启后才会清空, 可在一定程度防止误删除
mv foo1 /tmp
```


## touch
`touch`([触摸](https://dictionary.cambridge.org/us/dictionary/english-chinese-simplified/move)), 用于改变文件或目录的更新或访问时间和创建文件等.
```
# 改变文件更新时间
$ ls -l
total 4
-rw-rw-r-- 1 ho ho 15 Oct 12 08:30 foo3
$ touch foo3
$ ls -l
total 4
-rw-rw-r-- 1 ho ho 15 Oct 12 10:18 foo3

# 创建单个文件
$ ls
foo3
$ touch foo4
$ ls
foo3  foo4

# 创建多个文件
$ touch foo5 foo6
$ ls
foo3  foo4  foo5  foo6

# touch if exists
$ touch -c foo7
$ ls
foo3  foo4  foo5  foo6
```

## du
```
# 查看 foo 目录占用空间
du -sh foo

# 查看当前目录所有文件/目录占用空间
du -sh *

# 显示磁盘占用
df -h

# 清理旧版本缓存
apt-get autoclean

# 清理所有缓存
apt-get clean

# 移除孤立软件
apt-get autoremove

# 删除所有log
rm -rf /var/log/*

# 列出所有大于100M的文件
find / -size +100M
```

## 系统信息

http://blog.51cto.com/liguxk/152912

```
# 查看内核/操作系统/CPU信息
uname -a

# 查看操作系统版本
head -n 1 /etc/issue

# 查看CPU信息
cat /proc/cpuinfo

# ubuntu
lsb_release -a
```

## file hash
```
 
md5sum filename
sha1sum filename
sha256sum filename
sha512sum filename
```

## 辅助
### [explainshell.com](https://explainshell.com/explain?cmd=echo+%22Hello+world%21%22)

这是一个用来解释shell命令的网站, 在输入框中输入命令回车, 网站就会对命令各部分的解释给出参考

![explainShell.png](https://upload-images.jianshu.io/upload_images/4430947-d75168e6846b5936.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## [TL;DR](https://github.com/tldr-pages/tldr)
TL;DR是"Too Long; Didn't Read"的缩写, 这是一个帮助开发者查询命令常见用法的项目, 有[WEB](https://tldr.ostera.io)和shell(使用前需要用npm安装)两个端.

![tldrWeb.png](https://upload-images.jianshu.io/upload_images/4430947-ba16c1407a78a587.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
$ tldr mv

  mv

  Move or rename files and directories.

  - Move files in arbitrary locations:
    mv source target

  - Do not prompt for confirmation before overwriting existing files:
    mv -f source target

  - Do not prompt for confirmation before overwriting existing files but write t                                                                                            o standard error before overriding:
    mv -fi source target

  - Move files in verbose mode, showing files after they are moved:
    mv -v source target
```


参考链接:

[Basic ‘ls’ Command Examples in Linux](https://www.tecmint.com/15-basic-ls-command-examples-in-linux/)

[Basic Cat Command Examples in Linux](https://www.tecmint.com/15-basic-ls-command-examples-in-linux/)

[8 Practical Examples of Linux “Touch” Command](https://www.tecmint.com/8-pratical-examples-of-linux-touch-command/)