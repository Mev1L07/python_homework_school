# 猜数字小游戏：随机生成 100-999 的整数，反复猜直到猜中（带输入校验）
import random

x = random.randint(100, 999)

while True:
    p = input("从100到999里猜一个数字：")
    try:
        answer = int(p)
    except ValueError:
        print("请输入数字")
        continue        # 输入非法就重新猜

    if answer > x:
        print("大了")
    elif answer < x:
        print("小了")
    else:
        print(f"猜对了！答案是 {x}")
        break           # 猜对就结束
