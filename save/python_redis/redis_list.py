#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   redis_list.py
@Time    :   2020/04/18 18:05:56
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

# lpush(name,values)
# 在name对应的list中添加元素，每个新的元素都添加到列表的最左边

r.lpush("list1", 11, 22, 33)
r.lpush("list1", 12)
print(r.lrange('list1', 0, -1))#取出来，从第一个到最后一个
print("\n---------------------------------\n")

r.rpush("list2", 44, 55, 66)    # 在列表的右边，依次添加44,55,66
print(r.llen("list2"))  # 列表长度
print(r.lrange("list2", 0, -1)) # 切片取出值，范围是索引号0到-1(最后一个元素)
print("\n---------------------------------\n")

# lpushx(name,value)
# 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最左边
r.lpushx("list10", 10)   # 这里list10不存在
print(r.llen("list10"))  # 0
print(r.lrange("list10", 0, -1))  # []
r.lpushx("list2", 77)   # 这里"list2"之前已经存在，往列表最左边添加一个元素，一次只能添加一个
print(r.llen("list2"))  # 列表长度
print(r.lrange("list2", 0, -1)) # 切片取出值，范围是索引号0到-1(最后一个元素
print("\n---------------------------------\n")

r.rpushx("list2", 99)   # 这里"foo_list1"之前已经存在，往列表最右边添加一个元素，一次只能添加一个
print(r.llen("list2"))  # 列表长度
print(r.lrange("list2", 0, -1)) # 切片取出值，范围是索引号0到-1(最后一个元素)
print("\n---------------------------------\n")

# linsert(name, where, refvalue, value))
'''
在name对应的列表的某一个值前或后插入一个新值
参数：
    name - redis的name
    where - BEFORE或AFTER
    refvalue - 标杆值，即：在它前后插入数据
    value - 要插入的数据
'''
r.linsert("list2", "before", "11", "00")   # 往列表中左边第一个出现的元素"11"前插入元素"00"
print(r.lrange("list2", 0, -1))   # 切片取出值，范围是索引号0-最后一个元素
print("\n---------------------------------\n")

# r.lset(name, index, value)
'''
对name对应的list中的某一个索引位置重新赋值
参数：
    name - redis的name
    index - list的索引位置
    value - 要设置的值
'''
r.lset("list2", 0, -11)    # 把索引号是0的元素修改成-11
print(r.lrange("list2", 0, -1))
print("\n---------------------------------\n")

# r.lrem(name, value, num)
'''
在name对应的list中删除指定的值
参数：
    name - redis的name
    value - 要删除的值
    num - num=0，删除列表中所有的指定值；
    num=2 - 从前到后，删除2个, num=1,从前到后，删除左边第1个
    num=-2 - 从后向前，删除2个
'''
r.lrem("list2", "11", 1)    # 将列表中左边第一次出现的"11"删除
print(r.lrange("list2", 0, -1))
r.lrem("list2", "99", -1)    # 将列表中右边第一次出现的"99"删除
print(r.lrange("list2", 0, -1))
r.lrem("list2", "22", 0)    # 将列表中所有的"22"删除
print(r.lrange("list2", 0, -1))
print("\n---------------------------------\n")

# lpop(name)
# 在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
r.lpop("list2")    # 删除列表最左边的元素，并且返回删除的元素
print(r.lrange("list2", 0, -1))
r.rpop("list2")    # 删除列表最右边的元素，并且返回删除的元素
print(r.lrange("list2", 0, -1))
print("\n---------------------------------\n")

# ltrim(name, start, end)
'''
在name对应的列表中移除没有在start-end索引之间的值
参数：
    name - redis的name
    start - 索引的起始位置
    end - 索引结束位置
'''
r.ltrim("list2", 0, 2)    # 删除索引号是0-2之外的元素，值保留索引号是0-2的元素
print(r.lrange("list2", 0, -1))
print("\n---------------------------------\n")

# lindex(name, index)
# 在name对应的列表中根据索引获取列表元素
print(r.lindex("list2", 0))  # 取出索引号是0的值
print("\n---------------------------------\n")

# rpoplpush(src, dst)
'''
从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边
参数：
    src - 要取数据的列表的 name
    dst - 要添加数据的列表的 name
'''
r.rpoplpush("list1", "list2")
print(r.lrange("list2", 0, -1))
print("\n---------------------------------\n")

# brpoplpush(src, dst, timeout=0)
'''
从一个列表的右侧移除一个元素并将其添加到另一个列表的左侧
参数：
    src - 取出并要移除元素的列表对应的name
    dst - 要插入元素的列表对应的name
    timeout - 当src对应的列表中没有数据时，阻塞等待其有数据的超时时间（秒），0 表示永远阻塞
'''
r.brpoplpush("list1", "list2", timeout=2)
print(r.lrange("list2", 0, -1))
print("\n---------------------------------\n")

# blpop(keys, timeout)
'''
将多个列表排列，按照从左到右去pop对应列表的元素
参数：
    keys - redis的name的集合
    timeout - 超时时间，当元素所有列表的元素获取完之后，阻塞等待列表内有数据的时间（秒）, 0 表示永远阻塞
r.brpop(keys, timeout) 同 blpop，将多个列表排列,按照从右像左去移除各个列表内的元素
'''
r.lpush("list10", 3, 4, 5)
r.lpush("list11", 3, 4, 5)
while True:
    r.blpop(["list10", "list11"], timeout=2)
    print(r.lrange("list10", 0, -1), r.lrange("list11", 0, -1))
print("\n---------------------------------\n")

