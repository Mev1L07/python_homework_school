# 用 f-string 格式化小数位数，以及 math.pi 的取值
import math

number = math.pi
print(number)
print(f"保留 6 位小数：{number:.6f}")
print(f"保留 4 位小数：{number:10.4f}")
print(f"保留 3 位小数：{number:.3f}")
