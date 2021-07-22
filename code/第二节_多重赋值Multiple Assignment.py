# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 19:50:37 2021

@author: wuzhe
"""

# 这里表示注释内容，用于程序员分析代码的作用，注释内容在编译过程中并不会被执行
######################### 上节回顾 ###########################
## 变量
age = 32            # int
height = 170.2      # float
name = "Tom"        # string
is_worker = True    # bool

# type(变量名称)表示分析变量的类型
print("age变量类型为: {}".format(type(age)))                # 分析变量类型
print("height变量类型为: {}".format(type(height))) 
print("name变量类型为: {}".format(type(name))) 
print("is_worker变量类型为: {}".format(type(is_worker))) 

print("--------------------------------------------------")
# 第二节：多重赋值
# 标准格式 -> 变量名称1, 变量名称2, ..., 变量名称n = 变量1的值, 变量2的值, ..., 变量n的值
# 作用：简化代码的书写过程，但是可读性变差
age, height, name, is_worker = 32, 170.2, "Tom", True
print("age={}, height={}, name={}, is_worker={}".format(age, height, name, is_worker))

print("--------------------------------------------------")
# 当多个变量取相同值时，我们使用多重赋值可以避免出错（推荐使用）
# 标准格式 -> 变量名称1=变量名称2= ...=变量名称n=取值
wang_age = huang_age = wu_age = 18
print("小王的年龄是: {}, 小黄的年龄是: {}, 小吴的年龄是: {}".format(wang_age, huang_age, wu_age))
