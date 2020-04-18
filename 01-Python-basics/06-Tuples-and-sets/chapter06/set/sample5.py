# 生成式
# 生成式语法: [被追加的数据 循环语句 循环或者判断语句]|{}
# 列表生成式
lst1 = []
for i in range(10, 20):
    lst1.append(i * 10)
print(lst1)

lst2 = [i * 10 for i in range(10, 20)]
print(lst2)

lst3 = [i * 10 for i in range(10, 20) if i % 2 == 0]
print(lst3)

for i in range(10, 20):
    if i % 2 == 0:
        lst3.append(i * 10)

lst4 = [i * j for i in range(1, 5) for j in range(1, 5)]
print(lst4)

for i in range(1, 5):
    for j in range(1, 5):
        lst4.append(i * j)

# 字典生成式
lst5 = ['张三', '李四', '王五']
dict1 = {i + 1: lst5[i] for i in range(0, len(lst5))}
print(dict1)

for i in range(0, len(lst5)):
    dict1[i + 1] = lst5[i]

# 集合生成式
set1 = {i * j for i in range(1, 4) for j in range(1, 4) if i == j}
print(set1)

for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            set1.add(i * j)
