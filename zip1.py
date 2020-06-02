"""
描述：Python内置函数--zip函数01
参考：https://www.runoob.com/python3/python3-func-zip.html
作者：王佳秋
日期：2020年5月29日
"""

if __name__ == "__main__":

    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [4, 5, 6, 7, 8]
    zipped = zip(a, b)  # 返回一个对象
    print("zip对象：", zipped)
    print("将zip对象转换成列表：", list(zipped))
    zipped2 = zip(a, c)  # 元素个数与最短的列表一致
    print("zipped2: ", list(zipped2))

    # print(zip(*zip(a, b)))  # 利用 * 号操作符，可以将元组解压为列表。
    # 与zip相反，zip(*)可理解为解压，返回二维矩阵式
    a1, a2 = zip(*zip(a, b))
    print("a1: ", a1)
    print("a2: ", a2)
    print(list(a1))
    print(list(a2))

    # 三个iterable的压缩
    zipped3 = zip(a, b, c)
    print(list(zipped3))
