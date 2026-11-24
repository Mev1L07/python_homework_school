# 自定义无返回值函数，循环调用 5 次打印同一个值
def f1(a):
    print(a)


s=input("请输入一个值: ")
for x in range(1, 6):
    f1(s)