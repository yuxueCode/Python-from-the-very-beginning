

def f(n):
    """ 判断给定的数是不是寄数 """
    return n % 2 != 0


def use_filer(l):
    """
    获取指定列表/元祖中的奇数
    :param l: list/tuple 要过滤的数据
    :return: 过滤好的奇数列表
    """
    # rest = filter(lambda n: n % 2 != 0, l)
    rest = filter(f, l)
    return rest


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    rest = use_filer(l)
    print(list(rest))
