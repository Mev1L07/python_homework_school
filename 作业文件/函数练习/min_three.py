# 自定义函数求两个数最小值，嵌套调用求三个数的最小值（作业题）
def f3(x, y):
    if x < y:
        return x
    else:
        return y

a = int(input("请输入第1个整数: "))
b = int(input("请输入第2个整数: "))
c = int(input("请输入第3个整数: "))

print(f"三个数的最小值是 {f3(f3(a, b), c)}")
