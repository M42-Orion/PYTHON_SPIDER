import json

str = '''
[{
    "name": "Tom",
    "gender": "male"
}, {
    "name": "Jack",
    "gender": "male"   
}]
'''
#将字符串转为json格式
print(type(str))
data = json.loads(str)
print(type(data))
print(data)