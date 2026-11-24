# 猴子吃桃问题：倒推第一天摘了多少个桃子
peaches=1
for i in range(9):
    peaches = (peaches + 1) * 2
print(peaches)