x=[{"name":"张一","age":18},{"name":"李二","age":3},{"name":"王三","age":80}]
for i in x:
    if i["age"] >= 18:
        print(f"{i['name']} 是成年人，今年 {i['age']} 岁。")
    else:
        print(f"{i['name']} 不是成年人，今年 {i['age']} 岁。")