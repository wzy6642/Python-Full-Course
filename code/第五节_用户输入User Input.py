# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:11:04 2021

@author: wuzhe
"""

# 之前都是直接定义变量，但是在实际应用中，很多时候都需要用户输入
# 例如，你在注册账户的时候，需要输入用户昵称、性别、年龄、出生日期
# 代码的核心想法是和用户交互，也就是让用户能够参与其中
# 所以这个时候，我们就需要学习如何让用户输入数据，并将这些数据使用起来，供我们进一步分析
# 第五节 用户输入input()
# 注意：input()的返回结果均是字符串类型，如果需要转换为其他类型，那就需要用到上一节的强制类型转换

# 案例一：让用户输入姓名
name = input("请输入您的姓名：")
print("用户的姓名为：{}".format(name))

# 案例二：让用户输入年龄
age = input("请输入您的年龄：")
age = int(age)
age = age + 1
print("用户的年龄为：{}岁".format(age))

# 案例三：让用户输入身高
height = input("请输入您的身高：")
height = float(height)
height = height + 1
print("用户的身高为：{}cm".format(height))

# 案例四：让用户输入是否是工人
# 直接回车才为空，这时候打印False，除此之外，都是True
is_worker = input("请问您是否是工人(True/'')：")
is_worker = bool(is_worker)
print("用户是否是工人：{}".format(is_worker))

