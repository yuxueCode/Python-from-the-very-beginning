# 函数的形参与实参
# 参数就是函数的输入数据,在程序运行时根据参数不同执行不同代码
def print_verse(verse_name, is_show_title, is_show_dynasty):
    # 函数体
    if verse_name == "静夜思":
        if is_show_title == True:
            print("静夜思-李白")
        if is_show_dynasty == True:
            print("唐朝")
        print("床前明月光")
        print("疑是地上霜")
        print("举头望明月")
        print("低头思故乡")
    elif verse_name == "再别康桥":
        if is_show_title == True:
            print("再别康桥-徐志摩")
        if is_show_dynasty == True:
            print("民国")
        print("轻轻地我走了")
        print("正如我轻轻地来")
        print("挥一挥手")
        print("不带走一片云彩")


print_verse("静夜思", True, False)

print("...")

print_verse("再别康桥", True, True)
