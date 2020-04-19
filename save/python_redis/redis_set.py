#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   redis_set.py
@Time    :   2020/04/19 13:03:16
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

# sadd(name,values)
# name - 对应的集合中添加元素
r.sadd("set1", 33, 44, 55, 66)  # 往集合中添加元素
print(r.scard("set1"))  # 集合的长度是4
print(r.smembers("set1"))   # 获取集合中所有的成员
print("\n--------------------------\n")

# scard(name)
# 获取name对应的集合中元素个数
print(r.scard("set1"))  # 集合的长度是4
print("\n--------------------------\n")

# smembers(name)
# 获取name对应的集合的所有成员
print(r.smembers("set1"))   # 获取集合中所有的成员

# 获取集合中所有的成员--元组形式
# sscan(name, cursor=0, match=None, count=None)
print(r.sscan("set1"))

# 获取集合中所有的成员--迭代器的方式
# sscan_iter(name, match=None, count=None)
# 同字符串的操作，用于增量迭代分批获取元素，避免内存消耗太大
for i in r.sscan_iter("set1"):
    print(i)
print("\n--------------------------\n")

# sdiff(keys, *args)
# 在第一个name对应的集合中且不在其他name对应的集合的元素集合
r.sadd("set2", 11, 22, 33)
print(r.smembers("set1"))   # 获取集合中所有的成员
print(r.smembers("set2"))
print(r.sdiff("set1", "set2"))   # 在集合set1但是不在集合set2中
print(r.sdiff("set2", "set1"))   # 在集合set2但是不在集合set1中
print("\n--------------------------\n")

# sdiffstore(dest, keys, *args)
# 获取第一个name对应的集合中且不在其他name对应的集合，再将其新加入到dest对应的集合中
r.sdiffstore("set3", "set1", "set2")    # 在集合set1但是不在集合set2中
print(r.smembers("set3"))   # 获取集合3中所有的成员
print("\n--------------------------\n")

# sinter(keys, *args)
# 获取多一个name对应集合的交集
print(r.sinter("set1", "set2")) # 取2个集合的交集
print("\n--------------------------\n")

# sinterstore(dest, keys, *args)
# 获取多一个name对应集合的并集，再将其加入到dest对应的集合中
print(r.sinterstore("set3", "set1", "set2")) # 取2个集合的交集
print(r.smembers("set3"))

# 并集
# sunion(keys, *args)
# 获取多个name对应的集合的并集
print(r.sunion("set1", "set2")) # 取2个集合的并集

# 并集--并集存在一个新的集合
# sunionstore(dest,keys, *args)
# 获取多一个name对应的集合的并集，并将结果保存到dest对应的集合中
print(r.sunionstore("set3", "set1", "set2")) # 取2个集合的并集
print(r.smembers("set3"))
print("\n--------------------------\n")

# 判断是否是集合的成员 类似in
# sismember(name, value)
# 检查value是否是name对应的集合的成员，结果为True和False
print(r.sismember("set1", 33))  # 33是集合的成员
print(r.sismember("set1", 23))  # 23不是集合的成员
print("\n--------------------------\n")

# 移动
# smove(src, dst, value)
# 将某个成员从一个集合中移动到另外一个集合
r.smove("set1", "set2", 44)
print(r.smembers("set1"))
print(r.smembers("set2"))
print("\n--------------------------\n")

# 删除--随机删除并且返回被删除值
# spop(name)
# 从集合移除一个成员，并将其返回,说明一下，集合是无序的，所有是随机删除的
print(r.spop("set2"))   # 这个删除的值是随机删除的，集合是无序的
print(r.smembers("set2"))
print("\n--------------------------\n")

# 删除--指定值删除
# srem(name, values)
# 从集合移除一个成员，并将其返回,说明一下，集合是无序的，所有是随机删除的
print(r.spop("set2"))   # 这个删除的值是随机删除的，集合是无序的
print(r.smembers("set2"))
print("\n--------------------------\n")

# 删除--指定值删除
# srem(name, values)
# 在name对应的集合中删除某些值
print(r.srem("set2", 11))   # 从集合中删除指定值 11
print(r.smembers("set2"))
