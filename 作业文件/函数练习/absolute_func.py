def f3(a):
    if a > 0:
        return a
    elif a < 0:
        return -a
    else:
        return 0

x = float(input("请输入一个数: "))
print(f"{x} 的绝对值是 {f3(x)}")