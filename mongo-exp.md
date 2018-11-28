# mongo 空间管理
## 碎片整理
[StackOverflow - MongoDB - file size is huge and growing](https://stackoverflow.com/questions/6263729/mongodb-file-size-is-huge-and-growing)

已删除的 obj 仍然占用空间。

```
db.repairDatabase()
```

## 关闭/限制 journal 日志
[StackOverflow - Is it safe to delete the journal file of mongodb?](https://stackoverflow.com/questions/19533019/is-it-safe-to-delete-the-journal-file-of-mongodb)
```
# 备份原设置
cp -p /etc/mongodb.conf /etc/mongodb.conf.orig
nano /etc/mongodb.conf

# 方式1 禁用 journal
# journal=false

# 方式2 使用 smallfiles
smallfiles=true
into the mongodb.conf, then save. smallfiles limits the journal file to 128MB.


# 重启
service mongodb stop
rm -rf /var/lib/mongodb/journal/*
service mongodb start
```

## 启动失败
[StackOverflow - can't start mongodb as sudo](https://stackoverflow.com/questions/6819852/cant-start-mongodb-as-sudo)