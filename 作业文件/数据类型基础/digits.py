# 输入一个整数，把它拆成各个数位（列表推导式）
number = int(input("请输入一个整数："))
digits = [int(digit) for digit in str(abs(number))]

print(f"各个数位是：{digits}")
