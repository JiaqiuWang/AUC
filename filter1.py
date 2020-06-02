"""
描述：Python内置函数--filter函数01；用于过滤序列
参考：https://www.runoob.com/python3/python3-func-filter.html
作者：王佳秋
日期：2020年5月31日
"""

import math


def is_odd(n):
    """过滤出列表中的所有奇数"""
    print("计算值：", n % 2 == 1)
    return n % 2 == 1  # 除余方法


def is_sqr(x):
    """过滤1~100中平方根是整数的数"""
    # print("平方根：", math.sqrt(x))
    return math.sqrt(x) % 1 == 0


if __name__ == "__main__":
    print("输出方法描述：", is_odd.__doc__)
    tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    newlist = list(tmplist)
    print("过滤后的list: ", newlist)
    print()

    print("输出方法描述：", is_sqr.__doc__)
    tmplist = filter(is_sqr, range(1, 101))
    newlist = list(tmplist)
    print("过滤后的list: ", newlist)
