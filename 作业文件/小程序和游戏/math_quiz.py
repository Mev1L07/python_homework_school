# 两位数加法小测验：随机生成两个两位数，输入答案判断对错
import random

x = random.randint(10, 99)
y = random.randint(10, 99)
print(f"{x}+{y}=?")

p = input("请输入你的计算结果")

try:
    answer = int(p)
except ValueError:
    print("请输入数字 buddy")
else:
    if x + y == answer:
        print("right")
    else:
        print("u are so stupid buddy")
