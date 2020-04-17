# 列表的写操作
persons = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']
# 列表的追加
persons.append("杨九")
print(persons)
# 列表的插入
persons.insert(2 , '刘二')
print(persons)
persons.insert(len(persons) , '候大')
print(persons)

# 列表的更新
persons[2] = '宋二'
print(persons)
# 列表范围取值是"左闭右开"
persons[3:5] = ['王五','李四']
print(persons)

# 列表的删除操作
# 按元素内容删除
persons.remove('宋二')
print(persons)
# 按索引值删除元素
persons.pop(4)
print(persons)
# 范围删除
persons[4:7] = []
print(persons)