#break
i = 0
while i < 3:
    mobile = input("请输入您要查询的手机号：")
    i = i + 1
    if mobile == "13312345678":
        print("您的话费余额为158元")
        break
print("感谢您的来电")
