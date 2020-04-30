import random
from datetime import datetime


def write_file():
    """ 写入文件 """
    file_name = 'write_test.txt'
    # 以写入的方式打开文件
    f = open(file_name, 'w')
    # 写入一行内容
    f.write('hello')
    # 换行符\n \r \r\n
    f.write('\n')
    # 再写入一行内内容
    f.write('world')

    # 关闭文件
    f.close()


def write_mult_line():
    """ 向文件中写入多行内容 """
    file_name = 'write_mult_line.txt'
    with open(file_name, 'w', encoding='utf-8') as f:
        l = ['第一行', '\n', '第二行', '\r\n', '第三行']
        f.writelines(l)


def write_user_log():
    """ 记录用户的日志 """
    # 记录时间 + 记录用户的ID
    rest = '用户：{0} - 访问时间 {1}'.format(random.randint(1000, 9999), datetime.now())
    print(rest)
    # 文件名称
    file_name = 'write_user_log.txt'
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(rest)
        f.write('\n')


def read_and_write():
    """ 先读，再写入 """
    file_name = 'read_and_write.txt'
    with open(file_name, 'r+', encoding='utf-8') as f:
        read_rest = f.read()
        # 如果有1，写入一行数据bbb
        # 如果里面没有1，就写一行数据 aaa
        if '1' in read_rest:
            f.write('bbbb')
        else:
            f.write('aaaa')
        f.write('\n')



if __name__ == '__main__':
    # write_file()

    # write_mult_line()

    # write_user_log()

    read_and_write()