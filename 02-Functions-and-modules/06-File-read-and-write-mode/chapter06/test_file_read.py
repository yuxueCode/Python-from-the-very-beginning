

def read_file():
    """ 读取文件 """
    file_name = 'test.txt'
    # 使用绝对路径
    file_path = 'C:\\Users\\yima1\\Desktop\\py_learn\\chapter04\\test.txt'
    file_path2 = '/Users/yima1/Desktop/py_learn/chapter04/test.txt'

    # 使用普通的方式来打开文件
    with open(file_path2, encoding='utf-8') as f:
        # 读文件所有内容
        # rest = f.read()
        #
        # # 读取指定的几个内容
        # rest = f.read(8)
        # print(rest)
        # print(f.read(8))

        # # 随机读取
        # f.seek(10)
        # print(f.read(5))

        # 按行读取
        # rest = f.readline(8)
        # print(rest)
        # print(f.readline(8))
        # # print(f.readline())

        # 读取所有行
        rest = f.readlines(4)
        print(len(rest))
        for i in rest:
            print(i)


        # # 关闭文件
        # f.close()


if __name__ == '__main__':
    read_file()
