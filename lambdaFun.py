"""
描述：匿名函数lambda
参考：https://www.runoob.com/python3/python3-function.html
作者：王佳秋
日期：2020年5月31日
"""

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2


if __name__ == "__main__":
    # 调用sum 匿名函数
    print("相加后的值为：", sum(10, 20))
    print("相加后的值为：", sum(20, 20))
