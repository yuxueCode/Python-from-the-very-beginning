emp1 = {'name':'Jacky' , 'grade' : 'B'}
emp2 = {'name':'Lily' , 'grade' : 'A'}
# 1. setdefault为字典设置默认值,如果某个key已存在则忽略,如果不存在则设置
emp1.setdefault('grade' , 'C')
emp2.setdefault('grade' , 'C')

#if 'grade' not in emp2:
#    emp2['grade'] = 'C'
print(emp2)

# 2. 获取字典的视图
# (1) keys 代表获取所有的键
ks = emp1.keys()
print(ks)
print(type(ks))
# (2) values 代表获取所有的值
vs = emp1.values()
print(vs)
print(type(vs))
# (3) items 代表获取所有的键值对
its = emp1.items()
print(its)
print(type(its))

emp1['hiredate'] = '1984-05-30'
print(ks)
print(vs)
print(its)

# 3. 利用字典格式化字符串
# 老版本的字符串格式化
emp_str = "姓名:%(name)s,评级:%(grade)s,入职时间:%(hiredate)s" %emp1
print(emp_str)

# 新版本的字符串格式化
emp_str1 = "姓名:{name},评级:{grade},入职时间:{hiredate}".format_map(emp1)
print(emp_str1)