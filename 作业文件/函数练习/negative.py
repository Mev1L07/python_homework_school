# 自定义函数求一个数的相反数
def f3(a):
    return -a

x = float(input("请输入一个数: "))
result = f3(x)
print(f"{x} 的相反数是 {result}")