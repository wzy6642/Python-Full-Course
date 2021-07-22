# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 20:31:13 2021

@author: wuzhe
"""

# 第三节：字符串方法(str)
# 我们创建一个变量用于存储用户的手机号码
phone_number = "890-2345-123"
# len()用于求取字符串的长度
print("手机号码字符串的长度为: {}".format(len(phone_number)))
# find()求取某一字符在字符串中的位置
# 在Python中，序列的位次从0开始标记
# 890-2345-123
# 0123456789
print("8的位置是: {}".format(phone_number.find("8")))
# 对于重复出现的元素，只返回其第一次出现时的位置
print("-的位置是: {}".format(phone_number.find("-")))
# 字符串首字母大写，其余字母均小写，通常用于对姓名的处理
name = "tOM"
print("首字母大写的运行结果: {}".format(name.capitalize()))
# 字符串所有字母大写
print("所有字母大写的运行结果: {}".format(name.upper()))
# 字符串中所有字母小写
print("所有字母小写的运行结果: {}".format(name.lower()))
# 判断字符串表示内容是否是数字
print("姓名是数字吗？ {}".format(name.isdigit()))
print("123是数字吗？ {}".format("123".isdigit()))
# 判断字符串表示内容是否是字母
print("姓名是字母吗？ {}".format(name.isalpha()))
print("123是字母吗？ {}".format("123".isalpha()))
# 计算字符串中某元素出现的次数
print("字母t在姓名中出现了{}次".format(name.count("t")))
# 替换字符串中某个元素，replace(要被替换的元素, 替换后的元素)
print("将字符串中的t替换为b：{}".format(name.replace("t", "b")))
# 将字符串复制多次
print("字符串复制5次：{}".format(name*5))

