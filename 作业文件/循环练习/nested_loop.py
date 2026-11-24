# 双重 for 循环：打印九九乘法表
for n in range(1,10):
    for x in range(1,n+1):
        print(f"{x}*{n}={x*n}", end="\t")
    print()