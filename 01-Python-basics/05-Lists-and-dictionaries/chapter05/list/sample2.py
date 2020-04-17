# 列表的取值
list = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']
print(list)
# 取值的语法: 变量 = 列表变量[索引值]
zhaoliu = list[3]
print(zhaoliu)
zhaoliu = list[-3]
print(zhaoliu)

# 范围取值: 列表变量 = 原列表变量[起始索引:结束索引]
# 在Python中列表范围取值是"左闭右开"
list1 = list[1: 4]
print(list1)
print(list1[-1])

# 列表的index函数用于获取指定元素的索引值
zhaoliu_index = list.index('赵六')
print(zhaoliu_index)
