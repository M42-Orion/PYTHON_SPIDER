#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   redis_set.py
@Time    :   2020/04/18 00:16:40
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
import redis
import time


'''
Set操作，Set集合就是不允许重复的列表，本身是无序的。
有序集合，在集合的基础上，为每元素排序；元素的排序需要根据另外一个值来进行比较，所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序。
'''
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# hset(name, key, value)
'''
name对应的hash中设置一个键值对（不存在，则创建；否则，修改）
参数：
    name - redis的name
    key - name对应的hash中的key
    value - name对应的hash中的val
'''
r.hset("hash1", "k1", "v1")
r.hset("hash1", "k2", "v2")
print(r.hkeys("hash1")) # 取hash中所有的key
print(r.hget("hash1", "k1"))    # 单个取hash的key对应的值
print(r.hmget("hash1", "k1", "k2")) # 多个取hash的key对应的值
r.hsetnx("hash1", "k2", "v3") # 只能新建
print(r.hget("hash1", "k2"))

print("\n--------------------\n")
# hmset(name, mapping)
'''
在name对应的hash中批量设置键值对
参数：
    name - redis的name
    mapping - 字典，如：{'k1':'v1', 'k2': 'v2'}
'''
r.hmset("hash2", {"k2": "v2", "k3": "v3"})

print("\n--------------------\n")
# hmget(name, keys, *args)
'''
在name对应的hash中获取多个key的值
参数：
    name - reids对应的name
    keys - 要获取key集合，如：['k1', 'k2', 'k3']
    *args - 要获取的key，如：k1,k2,k3
'''
print(r.hget("hash2", "k2"))  # 单个取出"hash2"的key-k2对应的value
print(r.hmget("hash2", "k2", "k3"))  # 批量取出"hash2"的key-k2 k3对应的value --方式1
print(r.hmget("hash2", ["k2", "k3"]))  # 批量取出"hash2"的key-k2 k3对应的value --方式2

print("\n--------------------\n")
# hgetall(name)
# 获取name对应hash的所有键值
print(r.hgetall("hash1"))

print("\n--------------------\n")
# hlen(name)
# 获取name对应的hash中键值对的个数
print(r.hlen("hash1"))

print("\n--------------------\n")
# hkeys(name)
# 获取name对应的hash中所有的key的值
print(r.hkeys("hash1"))

print("\n--------------------\n")
# hvals(name)
# 获取name对应的hash中所有的value的值
print(r.hvals("hash1"))

print("\n--------------------\n")
# hexists(name, key)
# 检查 name 对应的 hash 是否存在当前传入的 key
print(r.hexists("hash1", "k4"))  # False 不存在
print(r.hexists("hash1", "k1"))  # True 存在

print("\n--------------------\n")
# hdel(name,*keys)
# 将name对应的hash中指定key的键值对删除
print(r.hgetall("hash1"))
r.hset("hash1", "k2", "v222")   # 修改已有的key k2
r.hset("hash1", "k11", "v1")   # 新增键值对 k11
r.hdel("hash1", "k1")    # 删除一个键值对
print(r.hgetall("hash1"))

print("\n--------------------\n")
# hincrby(name, key, amount=1)
'''
自增name对应的hash中的指定key的值，不存在则创建key=amount
参数：
    name - redis中的name
    key - hash对应的key
    amount - 自增数（整数）
'''
r.hset("hash1", "k3", 123)
r.hincrby("hash1", "k3", amount=-1)
print(r.hgetall("hash1"))
r.hincrby("hash1", "k4", amount=1)  # 不存在的话，value默认就是1
print(r.hgetall("hash1"))

print("\n--------------------\n")
# hincrbyfloat(name, key, amount=1.0)
'''
自增name对应的hash中的指定key的值，不存在则创建key=amount
参数：
    name - redis中的name
    key - hash对应的key
    amount，自增数（浮点数）
自增name对应的hash中的指定key的值，不存在则创建key=amount。
'''
r.hset("hash1", "k5", "1.0")
r.hincrbyfloat("hash1", "k5", amount=-1.0)    # 已经存在，递减-1.0
print(r.hgetall("hash1"))
r.hincrbyfloat("hash1", "k6", amount=-1.0)    # 不存在，value初始值是-1.0 每次递减1.0
print(r.hgetall("hash1"))

print("\n--------------------\n")
# hscan(name, cursor=0, match=None, count=None)
'''
增量式迭代获取，对于数据大的数据非常有用，hscan可以实现分片的获取数据，并非一次性将数据全部获取完，从而放置内存被撑爆
参数：
    name - redis的name
    cursor - 游标（基于游标分批取获取数据）
    match - 匹配指定key，默认None 表示所有的key
    count - 每次分片最少获取个数，默认None表示采用Redis的默认分片个数
如：
    第一次：cursor1, data1 = r.hscan('xx', cursor=0, match=None, count=None)
    第二次：cursor2, data1 = r.hscan('xx', cursor=cursor1, match=None, count=None)
    ...
    直到返回值cursor的值为0时，表示数据已经通过分片获取完毕
'''
print(r.hscan("hash1"))

print("\n--------------------\n")
