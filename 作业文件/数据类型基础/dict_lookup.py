# 字典遍历：用 items() 一次取出所有键值对
dict1={"a1":"18","a2":"20","a3":"22"}
'''for x in dict1.keys():
    print(x)

for x in dict1.values():
    print(x)

for x in dict1.items():
    print(x[0], x[1])

for x in dict1.items():
    print(x)

for x in dict1.keys():
    print(x,dict1[x])'''

for x,y in dict1.items():
    print(x,y)