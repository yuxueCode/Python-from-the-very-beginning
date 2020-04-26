import random
import sys
from datetime import datetime


# 游戏进入提示函数
def guide_page(guide_word):
    # 要输出的标题文字信息
    print('{0}欢迎进入{1}小游戏{0}'.format('*' * 11, guide_word))


# 产生指定区间随机数函数
def set_final_num(num1, num2):
    # num_list列表接收起始值、终止值
    num_list = [num1, num2]
    # 确保输入的值为数字, 并存入rest列表
    rest = list(filter(lambda n: all_num(n), num_list))
    # 判断是否相等
    if num_equal(rest):
        print("所产生的随机数字区间为: {}".format(rest))
        # 返回产生区间内的随机数
        rand = random.randint(int(num1), int(num2))
        print(rand)
        return rand


# 数字类型判断函数
def all_num(n):
    return n.isdigit()


# 数值相等判定函数
def num_equal(ls):
    # 若相等
    if ls[0] == ls[1]:
        print("您输入的区间数字相同!!请重新启动")
        sys.exit()
    else:
        return 1


# 自定义输入类型函数
def construct_range_value(s, e):
    # 将用户输入的区间起始值和终止值由str类型转换为int类型 以列表形式返回
    start = int(s)
    end = int(e)
    return [start, end]


# 自定义核查数值是否属于指定区间函数
def check_num_legal(num, s, e):
    # 利用条件语句判断输入数值是否在指定区间，若不在该区间内，则返回1
    area_list = construct_range_value(s, e)
    # 左右区间
    left = area_list[0]
    right = area_list[1]
    if not left < num < right:
        return 1


# 自定义日志写入函数
def write_record(times, value):
    """
    将玩家每一次猜测数字和本次猜测次数两项信息写入日志文件，要求：
    使用with语法操作日志文件，将获取到的参数和时间信息以追加方式写入日志文件
    """
    log = "{0}: 第{1}次您猜测的数字为: {2}\n".format(datetime.now(), times, value)
    file_name = 'record.txt'
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(log)


def main(rand1, s, e):
    # temp接收随机数
    temp = rand1
    # 猜测的次数
    times = 0
    while True:
        num = int(input("请输入您猜测的数字:"))
        if check_num_legal(num, s, e):
            print("对不起您输入的数字未在指定区间!!!")
            print("************")
            continue
        else:
            times += 1
            print("************")
            write_record(times, num)
            if num == temp:
                print("恭喜您!只用了{}次就赢得了游戏".format(times))
                break
            elif num < temp:
                print("Lower than the answer")
                continue
            elif num > temp:
                print("Higher than the answer")
                continue


if __name__ == '__main__':
    # 输出标题信息
    guide_page("数字猜猜猜")
    # 分别接收用户输入数字区间的起始值和终止值
    i = input("数字区间起始值:")
    j = input("数字区间终止值:")
    # 转换类型 ..
    # 调用set_final_num( )函数得到随机数
    rands = set_final_num(i, j)

    main(rands, i, j)



