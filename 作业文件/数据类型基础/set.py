# 集合运算：交集 &、并集 |、差集 -、对称差 ^
awa={1,5,8,10}
qwq={1,2,3,4,5}

'''for i in awa:
    print(i)'''

'''awa.update(qwq)'''

'''awa.remove(1)
awa.discard(1)'''

#交集，并集，差集
print(awa&qwq)
print(awa|qwq)
print(awa-qwq)
print(qwq-awa)
print(awa^qwq)
