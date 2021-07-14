# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 21:13:16 2021

@author: wuzhe
"""
# 第一节 变量Variables
# 变量的命名，命名规则——变量中只能出现数字0-9、字母A-Z、下划线_，不能以数字开头
# 变量的命名讲求言简意赅，例如我要表示用户的名称，应该将其命名为name，若要表示用户的年龄，就需要用age
# 如果一个变量意义较为复杂，例如表示用户1的年龄，我们应该命名为：user1_age
# 变量好比一个盒子，只有赋予真实的值才有实际意义，比如用户年龄为18岁，那么我们可以将其表示为：age=18
# 常见的变量类型有：整数int（例如18），浮点数float（例如170.2），字符串string（例如"Jiaqi Wu"），布尔型bool（True、False）
# 整数类型的变量
# 例如我们要表示用户的年龄，备注：+用于拼接两个字符串，例如"我要出去"+"玩耍"->'我要出去玩耍'
age = 20
# str()用于将其他类型的数据转换为字符串类型，此处是int->str
print("用户的年龄是"+str(age)+"岁")
print("用户的年龄是{}岁".format(age))

# 浮点数类型的变量
height = 170.5
print("你的身高是"+str(height)+"cm")
print("你的身高是{}cm".format(height))

# 字符串类型变量
name = "Jon"
print("我的名字是"+name)
print("我的名字是{}".format(name))

# 布尔型变量
is_student = True
print("是否是学生？"+str(is_student))
print("是否是学生？{}".format(is_student))

# 推荐的变量打印方式
# Spyder程序运行快捷键：Shift+Enter
print("我的名字是{}，是否是学生？{}".format(name, is_student))


