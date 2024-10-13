"""
    测试用模块
"""
author = '阿山'
Time = '2024-10-12'
def add(a, b):
    return a+b

def total(*args):
    """
    参数args：接受一个数字列表
    return：列表中每个元素平方的和
    """  # 函数内部注释须缩进
    result = 0
    for arg in args:
        result += arg**2
    return result