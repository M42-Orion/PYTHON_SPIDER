#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   PY_redis.py
@Time    :   2020/04/17 15:49:39
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
import redis

'''
edis 是一个 Key-Value 数据库，Value 支持 string(字符串)，list(列表)，set(集合)，zset(有序集合)，hash(哈希类型)等类型。
'''
# 连接池，使用 connection pool 来管理对一个 redis server 的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数 Redis，这样就可以实现多个 Redis 实例共享一个连接池。
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)#连接数据库

r = redis.Redis(host='localhost', port=6379, decode_responses=True)   
r.set('name', 'runoob')  # 设置 name 对应的值
print(r.get('name'))  # 取出键 name 对应的值

# r = redis.StrictRedis(host = "localhost",port = 6379,db = 0)
# r.set("foo","bar")
# print(r.get("foo"))
