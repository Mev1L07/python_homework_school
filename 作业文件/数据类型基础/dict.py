# 字典基础：创建、修改值、用 get() 取值（带默认值）
dict1 = {'name':'peipei julian ozima','age':'刚满18岁~','sex':'femboy'}
dict2 = {'name':'simon','age':'400','sex':'gayest'}
dict3 = {'name':'pasta','age':'20','sex':'lesbian'}

dict2['age']=2000000
print(dict1,dict2,dict3)
print(dict1.get('name',"nope"))
print(dict1.get('namee',"nope"))