def f4(a,b):
    if a<b:
        return a
    else:
        return b

text1=float(input("请输入一个数: "))
text2=float(input("请输入另一个数: "))
try:
    x=float(text1)
    y=float(text2)
except ValueError:
    print("输入的不是一个有效的数字")
else:
    print(f"{x} 和 {y} 中的最小值是 {f4(x,y)}")