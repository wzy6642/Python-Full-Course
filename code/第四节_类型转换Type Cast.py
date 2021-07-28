# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 回顾
# 1、变量：命名规则 -> 字母、数字、下划线组成
#    变量类型：int、str、float、bool
age = 10            # int
height = 170.2      # float
name = "Tom"        # str
is_worker = True    # bool
# 2、当多个变量取相同值时：变量1 = 变量2 = 变量3 = value
user1_age = user2_age = 10
#    当多个变量取相不同值时：变量1, 变量2 = value1, value2
name, age = "Tom", 16
# 使用format打印到控制台
print("user's age is {}".format(age))
# 字符串方法：计算长度、字母大写、字母小写、判断是否是字母、判断是否是数字
print("用户昵称的长度为：{}".format(len(name)))

# 第四节 类型转换
## 将其他类型转换为字符串型str()，任何类型都能转为字符串型
print("-------------------------------")
age = 16
print(type(age))
age = str(age)                  # 16 -> '16'
print(type(age), age)

print("-------------------------------")
height = 180.5
print(type(height))
height = str(height)            # 180.5 -> '180.5'
print(type(height), height)

print("-------------------------------")
is_student = True
print(type(is_student))
is_student = str(is_student)    # True -> 'True'
print(type(is_student), is_student)

## 将其他类型转换为整型int()，只有包含整数的字符串能转换为整型
print("-------------------------------")
age = "16"
print(type(age))
age = int(age)                  # '16' -> 16
print(type(age))
age = age + 1
print(age)

print("-------------------------------")
height = '198.7'
# print(type(height))
# 需要注意的是，小数字符串不能转变为整数
# height = int(height)
# print(type(height))
is_student = "True"
# print(type(is_student))
# 需要注意的是，布尔类型字符串不能转变为整数
# is_student = int(is_student)
# print(type(is_student))

# 将其他类型转换为浮点型float()
age = 16
print(type(age))
age = float(age)            # 16 -> 16.0
print(type(age), age)

print("-------------------------------")
height = "178.5"
print(type(height))
height = float(height)      # "178.5" -> 178.5
print(type(height), height)
# 需要注意的是，布尔类型字符串不能转变为浮点数

# 将其他类型转换为布尔型bool()，任何类型都能转换为布尔型
# 布尔型一般作为开关变量
print("-------------------------------")
age = 1
print(type(age))
age = bool(age)             # 只要非0就是True，否则为False
print(type(age), age)

print("-------------------------------")
height = 0.0
print(type(height))
height = bool(height)       # 只要非0就是True，否则为False
print(type(height), height)

print("-------------------------------")
name = "Tom"
print(type(name))
name = bool(name)           # 只要非空就是True，否则为False
print(type(name), name)

print("-------------------------------")
name = ""
print(type(name))
name = bool(name)           # 只要非空就是True，否则为False
print(type(name), name)



