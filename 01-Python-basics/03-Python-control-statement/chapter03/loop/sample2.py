#阶乘计算器
num = input("请输入要计算的数值(1-100):")
num = int(num)
if num >= 1 and num <=100:
    i = 1
    result = 1 #结果
    while i <= num:
        #1: result = 1 , i = 1 , 结果=1
        #2：result = 1 , i = 2 , 结果=2
        #3: result = 2 , i = 3 , 结果=6
        #4：result = 6 , i = 4 , 结果=24
        #5：result = 24 , i = 5 , 结果=120
        #20...
        result = result * i
        if i % 5 == 0:
            print("{}:{}".format(i,result))
        i = i + 1
    #不使用缩进的代码，代表while循环结束后继续执行的语句
    print("最终结果:{}".format(result))
else:
    print("请输入1-100有效数字")