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


# 备份与还原
```
# 将 localhost:27017 下名为 prop 的数据库 dump 到 /tmp/db_dump/ 下 会自动创建 /tmp/db_dump/prop/ 目录
# 压缩 /tmp/db_dump/prop/ 目录，输出为：/tmp/db_dump/db_backup.tar.gz
# 删除 dump 文件
# 解压 db_backup.tar.gz 到 /tmp/ 目录，最后 dump 文件还原至 /tmp/prop/ 目录
mongodump --host localhost:27017 -d prop -o /tmp/db_dump/ --quiet \
    && tar czf /tmp/db_dump/db_backup.tar.gz -C /tmp/db_dump/ prop \
    && rm -r /tmp/db_dump/prop/ \
    && tar xzf /tmp/db_dump/db_backup.tar.gz -C /tmp/

rm -r /tmp/prop/ && rm /tmp/db_dump/db_backup.tar.gz

```

如果需要指定 collection 的备份，可以使用下面的脚本
```
colls=( mycoll1 mycoll2 mycoll5 )

for c in ${colls[@]}
do
  mongodump -d mydb -c $c
done
```
