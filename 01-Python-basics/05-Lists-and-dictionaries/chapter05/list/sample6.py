# 其他常用方法
persons = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']

#统计出现次数
cnt = persons.count('赵六')
print(cnt)

#追加操作
#append将整个列表追加到末尾,extend则是将列表中的元素追加到原始列表末尾
persons.append(['杨九' ,'吴十'])
print(persons)
persons.extend(['杨九' , '吴十'])
print(persons)

#in(成员运算符) 运算符用于判断数据是否在列表中存在,存在返回True,不存在返回False
persons.remove('张三')
b = '张三' in persons
print(b)

#copy 函数用于复制列表
persons1 = persons.copy()
persons2 = persons
print(persons1)
#is 身份运算符用于判断两个变量是否指向同一块内存
print(persons1 is persons)
print(persons2 is persons)


#clear 用于清空列表
persons.clear()
print(persons)
print(persons1)
print(persons2)