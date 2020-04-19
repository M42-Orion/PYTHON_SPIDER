#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   redis_string.py
@Time    :   2020/04/17 16:05:19
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
import redis
import time


pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
'''
set(name, value, ex=None, px=None, nx=False, xx=False)
    ex - 过期时间（秒）
    px - 过期时间（毫秒）
    nx - 如果设置为True，则只有name不存在时，当前set操作才执行
    xx - 如果设置为True，则只有name存在时，当前set操作才执行
'''
# 这里过期时间是3秒，3秒后p，键food的值就变成None
r.set('food', 'mutton', ex=3)  #key是"food"value是"mutton"将键值对存入redis缓存
print(r.get('food'),end = "\n-----------------------\n")  # mutton 取出键food对应的值

# 过期时间是3豪秒，3毫秒后，键foo的值就变成None
r.set('food', 'beef', px=3)
print(r.get('food'),end = "\n-----------------------\n")

# 设置为True，则只有name不存在时，当前set操作才执行 （新建）
print(r.set("",'watermelon', nx=True),end = "\n-----------------------\n")    # True--不存在
# 如果键fruit不存在，那么输出是True；如果键fruit已经存在，输出是None

# 设置为True，则只有name存在时，当前set操作才执行 （修改）
print((r.set('fruit', 'watermelon', xx=True)),end = "\n-----------------------\n")   # True--已经存在
# 如果键fruit已经存在，那么输出是True；如果键fruit不存在，输出是None

# 设置时间
# setex(name, time, value)#秒
# psetex(name, time_ms, value)#毫秒
r.psetex("fruit3", 5000, "apple")
time.sleep(5)
print(r.get('fruit3'),end = "--时间\n-----------------------\n")  # 5000毫秒后，取值就从apple变成None

# 批量设置值与批量获取
r.mset({'k1': 'v1', 'k2': 'v2'})
# r.mset(k1="v1", k2="v2") # 这里k1 和k2 不能带引号 一次设置多个键值对
print(r.mget("k1", "k2"))   # 一次取出多个键对应的值
print(r.mget("k1"),end = "--批量设置\n-----------------------\n")

# getrange(key, start, end)
# 获取子序列（根据字节获取，非字符）
r.set("cn_name", "仿佛兮若轻云之蔽月，飘摇兮若流风之回雪") # 汉字
print(r.getrange("cn_name", 0, 2)) # 取索引号是0-2 前3位的字节
print(r.getrange("cn_name", 0, -1),end = "--获取子序列\n-----------------------\n") # 取所有的字节

# setrange(name, offset, value)
# 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
r.set("en_name", "abcdefg") # 汉字
r.setrange("en_name", 1, "ccc")
print(r.get("en_name"),end = "--修改字符串内容\n-----------------------\n")  # jccci 原始值是junxi 从索引号是1开始替换成ccc 变成 jccci

# strlen(name)
# 返回name对应值的字节长度（一个汉字3个字节）
print(r.strlen("foo"),end = "--获取字符串长度\n-----------------------\n")  # 4 'goo1'的长度是4

# append(key, value)
r.append("name", "haha")    # 在name对应的值junxi后面追加字符串haha
print(r.mget("name"),end = "--字符串添加内容\n-----------------------\n")