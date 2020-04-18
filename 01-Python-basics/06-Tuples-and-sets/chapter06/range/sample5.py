# 序列类型间的互相转换
l1 = ['a', 'b', 'c']
t1 = ('d', 'e', 'f')
s1 = 'abc123'
s2 = 'abc,123'
r1 = range(1, 40)
# list() - 转换为列表
l2 = list(t1)
print(l2)
print(list(s1))
print(s2.split(","))
print(list(r1))

# tuple() - 转换为元组
print(tuple(l1))
print(tuple(s1))
print(tuple(s2.split(",")))
print(tuple(r1))

# str函数用于将单个数据转为字符串 join对列表进行连接
print(str(l1))
print(",".join(l1))
print("|".join(t1)) #join必须要求所有元素都是字符串
s3 = "" #将包含数字的序列输出
for i  in r1:
    s3 += str(i)
print(s3)
