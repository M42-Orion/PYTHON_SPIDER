import csv

# # 列表写入
# with open('test.csv','w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id','name','age'])
#     writer.writerow(['0','小明','7'])
#     writer.writerow(['1','小红','9'])

with open('test.csv','w') as csvfile:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
    writer.writeheader
    writer.writerow({'id':1,'name':'小强','age':22})