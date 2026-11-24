# 用 keyword 模块列出 Python 所有关键字并判断是否为关键字
import keyword

print("Python 关键字：")
print(", ".join(keyword.kwlist))
print(f"'if' 是关键字吗？{keyword.iskeyword('if')}")
