from functools import reduce


def get_sum(l):
    """
    根据给定的列表，求里面各个数字的总和
    :param l: list/type 里面是整数
    :return: 列表所有项的和
    """
    rest = 0
    for i in l:
        rest += i
    return rest


def get_sum_use_py(l):
    """
    使用python内置的sum()进行求和
    :param l:
    :return:
    """
    return sum(l)


def f(m, n):
    """ 求两个数的和 """
    return m + n


def get_sum_use_reduce(l):
    """
    使用reduce进行求和
    :param l:
    :return:
    """
    return reduce(f, l)


def get_sum_use_lambda(l):
    """
    使用reduce + lambda进行求和
    :param l:
    :return:
    """
    return reduce(lambda m, n: m + n, l)


if __name__ == '__main__':
    l = [1, 2, 4, 6, 7, 8, 9]
    rest = get_sum(l)
    print(rest)
    print('--------------')
    rest_py = get_sum_use_py(l)
    print(rest_py)
    print('---------------')
    rest_reduce = get_sum_use_reduce(l)
    print(rest_reduce)
    print('------------')
    rest_lambda = get_sum_use_lambda(l)
    print(rest_lambda)

