#redis 基本操作
>查看列表长度

```
llen key
```
>删除指定key中的所有记录
```
ltrim key 1 0
```
>列出所有的key
 ```
keys *
 ```
>列出匹配的key
 ```
keys apple*
 ```

>查看key类型
 ```
type key
 ```

>Zset:有序的set，在集合的基础上进行延伸有序，其K是sring  V是一个键值对，这个键值对是分数score：V，并默认从小到大排序

>操作：

>【1 ： zadd/zrange/zrange .. withscores】（添加元素，查看元素，按分数查看分数和元素）

>zadd  zset01 60 v1 79 v2 81 v3 64 v4 87 v5：（向有序集合中添加值v1,v2,v3...,并附相应的值）

>zrange  zset01 0 -1：（查看zset01中的值，默认按分数从小到大排序） 

>zrange  zset01  0 -1 withscores：（查看zset01中的分数和值，默认按分数由小到大排序）
![](https://upload-images.jianshu.io/upload_images/2608446-e02ea281f611e442.png?imageMogr2/auto-orient/strip|imageView2/2/w/1082/format/webp)

#set
> 添加单个元素
 ```
redis> SADD bbs "discuz.net"
(integer) 1
 ```

> 添加重复元素
 ```
redis> SADD bbs "discuz.net"
(integer) 0
 ```
> 添加多个元素
 ```
redis> SADD bbs "tianya.cn" "groups.google.com"
(integer) 2

 ```
> 查看元素
 ```    
redis> SMEMBERS bbs
1) "discuz.net"
2) "groups.google.com"
3) "tianya.cn"
 ```