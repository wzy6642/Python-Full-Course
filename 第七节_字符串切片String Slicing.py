# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:21:00 2021

@author: wuzhe
"""
## 第七节 字符串切片String Slicing
# 字符串 -> 索引 -> 字符串的索引是从0开始

position = "陕西省西安市太白南路"
print("第一个位置的值是: {}".format(position[0]))

# 我们如何获取字符串的子字符串呢？
# 字符串（集合） -> 子字符串（子集） 关系：包含
# [start:stop] -> 包含start但是不包含stop
# 默认start=0，stop=len(position)
# 获取城市名称
city = position[3:6]                # 半闭区间
print("城市名称为: {}".format(city))

# 获取省会名称
# 0可以省略，也就是说：[0:3] = [:3]
print("省会名称为: {}".format(position[:3]))   
print("地名为: {}".format(position[3:])) 

# 步长
print("每隔一个读一个: {}".format(position[::2]))
print("每隔一个读一个: {}".format(position[4::2]))

# 从右往左用的位置编号为负数
print("从右往左: {}".format(position[-4:]))
print("逆序: {}".format(position[::-1]))
print("逆序: {}".format(position[-1:-11:-1]))

# 考虑将一个字符串赋值给另一个字符串
position_2 = position[:]
print("复制后的字符串为: {}".format(position_2))
# 原因是：在python中，字符串是不可变对象，
# 不能通过下标的方式直接赋值修改。
# 同样的不可变对象还有：数字、字符串和元组。
# position_2[2] = "朔"         # 修改字符中索引为2的值为"朔" 
# TypeError: 'str' object does not support item assignment
position_2 = position_2.replace('西', '朔')  # (old, new) 用new替换old
print("修改后的字符串为: {}".format(position_2))
# 打印变量的内存地址
print(id(position))
print(id(position_2))





