# 字典的更新操作
employee = {'name': '王峰', 'sex': "男",
            'hiredate': '1997-10-20', 'grade': 'A',
            'job': '销售', 'salary': 1000,
            'welfare': 100
            }
print(employee)
#单个kv进行更新
employee['grade'] = 'B'
print(employee)
#对多个kv进行更新
employee.update(salary = 1200,welfare=150)
print(employee)

# 字典的新增操作与更新操作完全相同,秉承有则更新,无则新增的原则
employee['dept'] = '研发部'
print(employee)
employee['dept'] = '市场部'
print(employee)
employee.update(weight=80,dept='财务部')
print(employee)

# 与删除相关的函数
# 1. pop 删除指定的kv
employee.pop('weight')
print(employee)

# 2.popitem 删除最后一个kv
kv = employee.popitem()
kv = employee.popitem()

print(kv)
print(employee)

# 3. clear 清空字典
employee.clear()
print(employee)