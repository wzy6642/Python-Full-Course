# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:09:54 2021

@author: wuzhe
"""
## 第六节: math包的使用
# 什么是包？Python默认包含很多函数供用户使用，这样子就方便于我们快速开发程序
# 为了方便用户知道什么函数在哪一个具体文件下，Python定义包，一个包中包含了
# 诸多函数，但他们均具备某一类功能。
# Life is short, You need Python.
import math


# 常数
PI = math.pi
print("PI的取值为: {}".format(PI))

# 根式运算sqrt()
print("PI开方等于: {}".format(math.sqrt(PI)))

# 四舍五入round()
print("PI四舍五入后的结果: {}".format(round(PI)))

# 向上取整ceil()
print("PI向上取整的计算结果: {}".format(math.ceil(PI)))

# 向下取整floor()
print("PI向下取整的计算结果: {}".format(math.floor(PI)))

# 取绝对值abs()
print("-5的绝对值为: {}".format(abs(-5)))

# 幂运算pow()
print("PI的3次幂为: {}".format(math.pow(PI, 3)))

# 求几个数中最大的一个max()
print("2,3,4中最大的是: {}".format(max(2, 3, 4)))

# 求几个数中最小的一个min()
print("2,3,4中最小的是: {}".format(min(2, 3, 4)))

# sin(theta) = y -> arcsin(y) = theta
# f(x) = y -> g(y) = x 我们称f,g互为反函数
print(math.asin(1)-math.pi/2)



