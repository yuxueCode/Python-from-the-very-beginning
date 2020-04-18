# 集合间的关系操作
s1 = {1, 2, 3, 4, 5, 6}
s2 = {6, 5, 4, 3, 2, 1}
# == 判断两个集合的元素是否完全相同
print(s1 == s2)

s3 = {4, 5, 6, 7}
s4 = {1, 2, 3, 4, 5, 7, 6, 8}
# issubset判断是否为"子集"
print(s3.issubset(s4))
# issuperset判断是否为"父集"
print(s4.issuperset(s3))

s5 = {6}
s6 = {1, 3, 5, 7, 9}
#isdisjoint 函数判断两个集合是否存在重复元素
#True 代表不存在重复元素,False则代表存在重复
print(s5.isdisjoint(s6))
