#等值判断
if 1 != 1:
    print("1不等于1")
else:
    print("1等于1")

b = 1 == 1
print(b)
print(1 == 1.0)
print("abc".lower() == "Abc".lower())
print(" abc".strip() == "abc")
print(1 == int("1"))
#数字与布尔表达式的等值比较
#数字0代表False，非0代表True

print(0 == False)
print(1 == True)

if 3-1:
    print("成立")
else:
    print("不成立")

