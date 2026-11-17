def f5(a,b):
    c=(a+b)*2
    s=a*b
    return c,s




x=float(input("请输入矩形的一条边"))
y=float(input("请输入矩形的另一条边"))
t=f5(x,y)
print(f"矩形的周长是{t[0]}，面积是{t[1]}")
