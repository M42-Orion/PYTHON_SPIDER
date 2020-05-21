import pymysql

# 连接database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123',
    database='test',
    charset='utf8')

# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
# 得到一个可以执行SQL语句并且将结果作为字典返回的游标
#cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 定义要执行的SQL语句
sql = """
select * from runoob_tbl
"""

# 执行SQL语句
cursor.execute(sql)

ret1 = cursor.fetchone()

# 关闭光标对象
cursor.close()

# 关闭数据库连接
conn.close()

print(ret1)