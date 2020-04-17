#循环嵌套
'''
口口口口
口口口口
口口口口
口口口口
'''

j = 0
while j < 4:
    i = 0
    while i < 4:
        print("口", end="")  # 结尾不换行
        i = i + 1
    j = j + 1
    print("")

