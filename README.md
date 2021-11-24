# [Python基础知识](https://lush-popcorn-60c.notion.site/0-bf2b433e0f1548d185d06913b3032768)

### 0.1 变量及数据类型

---

- 查看Python版本
    
    在操作系统的命令行界面运行Python时，要确认该Python版本是否与你要使用的版本相同
    
    ```python
    # 代码内部使用sys模块查询Python版本号
    import sys
    sys.version_info
    >>> sys.version_info(major=3, minor=6, micro=4, releaselevel='final', serial=0)
    sys.version
    >>> '3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 10:22:32) [MSC v.1900 64 bit (AMD64)]'
    ```
    
    ```bash
    # 在终端查看Python版本号
    C:\Users\wuzhe>python --version
    >>> Python 3.6.4 :: Anaconda, Inc.
    ```
    
- 变量类型
    
    装有数据的容器，命名规则：由字母、下划线和数字组成，且数字不能开头，推荐snake-case命名法，例如user_name、user_age
    
    ```python
    # -*- coding:utf-8 -*-
    first_name = "Aston"
    print(type(first_name ))
    >>> <class 'str'>
    ```
    
    | 名称 | 举例 |
    | --- | --- |
    | 字符串（str） | first_name = "Aston" |
    | 整型（int） | age = 21 |
    | 浮点型（float） | height = 178.5 |
    | 布尔型（bool） | worker = True |
    
    [Python编程基础：第一节 变量Variables_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118600345)
    
- 字符串方法
    
    ```python
    # Unicode码点所组成的序列
    name = "asTono"
    ```
    
    | 名称 | 举例 | 结果 |
    | --- | --- | --- |
    | 计算长度 | len(name) | 6 |
    | 元素位置查询 | name.find("a") | 0 |
    | 首字母大写 | name.capitalize() | Astono |
    | 所有字母大写 | name.upper() | ASTONO |
    | 所有字母小写 | name.lower() | astono |
    | 是否是数值 | name.isdigit() | False |
    | 是否是字母 | name.isalpha() | True |
    | 元素个数统计 | name.count("o") | 2 |
    | 元素替换 | name.replace("o", "a") | asTana |
    | 内容重复多次 | name*3 | asTonoasTonoasTono |
    | 切片 | name[0: -1: 2] | aTn |
    | 分隔切片 | name.split("T") | ['as', 'ono'] |
    
    [Python编程基础：第三节 字符串方法String Methods_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118671333)
    
    [Python编程基础：第七节 字符串切片String Slicing_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118682432)
    
- 用户输入
    
    用`input()`函数获取用户的键盘输入，函数的返回结果为字符串
    
    ```python
    age = int(input("How old are you?: "))
    ```
    
    [Python编程基础：第五节 用户输入User Input_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118681726)
    
- 逻辑运算
    
    ```python
    x = 5>3
    y = 5<3
    a = 3
    b = 4
    ```
    
    | 名称 | 运算法则 | 运算表达式 | 计算结果 |
    | --- | --- | --- | --- |
    | 与 | 同真才真，有假则假 | x and y | False |
    | 或 | 有真则真，同假才假 | x or y | True |
    | 非 | 真变假，假变真 | not x | False |
    | 相等 | 检查两个操作数的值是否相等，如果是则条件变为真 | a==b | False |
    | 不等 | 检查两个操作数的值是否相等，如果值不相等，则为真 | a!=b | True |
    | 大于 | 检查左操作数的值是否大于右操作数的值，如果是，则为真 | a>b | False |
    | 小于 | 检查左操作数的值是否小于右操作数的值，如果是，则为真 | a<b | True |
    | 大于等于 |  | a>=b | False |
    | 小于等于 |  | a<=b | True |
    
    [Python编程基础：第九节 逻辑运算Logical Operators_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118691790)
    
- 编程规范
    - 每行不超过79个字符
    - 对于占据多行的长表达式来说，除了首行之外的其余各行都应该在通常的缩进级别之上再加4个空格
    - 在同一份文件中，函数与类之间用两个空行隔开
    - 在同一个类中，方法与方法之间用一个空行隔开
    - 使用字典时，键与冒号之间不加空格，写在同一行的冒号和值之间应该加一个空格
    - 给变量赋值时，赋值符号的左边和右边各加一个空格，并且只加一个空格就好
    - 函数、变量及属性用小写字母来拼写，各单词之间用下划线相连，例如：user_name
    - 类（包括异常）命名时，每个单词的首字母均大写，例如：TransformerModel
    - 模块级别的常量，所有字母都大写，各单词之间用下划线相连，例如：ALL_NUM
    - 不要通过长度判断容器或序列是不是空的，例如不要通过if len(something) == 0判断something是否为[]或''等空值，而是应该采用if not something这样的写法来判断，因为Python会把空值自动评估为False
    - 如果表达式一行写不下，可以用括号将其括起来，而且要适当地添加换行与缩进以便于阅读
    - 多行表达式，应该用括号括起来，而不要用\符号续行
    - 文件中的import语句应该按顺序分成三个部分：首先引入标准库里面的模块，然后引入第三方模块，最后引入自己的模块。属于同一个部分的import语句按字母顺序排列

- 多重赋值
    
    为每一个变量赋予相应的值
    
    ```python
    # 不同取值
    name, age, is_worker = "Aston", 18, False
    # 相同取值
    zhang_age = li_age = wang_age = wu_age = 18
    # 判断变量是否存在: '变量名称' in vars()
    'user_name' in vars()
    >>> False
    'name' in vars()
    >>> True
    ```
    
    [Python编程基础：第二节 多重赋值Multiple Assignment_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118666953)
    
- 基础数值计算
    
    ```python
    import math
    import random
    pi = 3.14
    x = 1
    y = 2
    z = 3
    my_list = ['rock', 'paper', 'scissors']
    ```
    
    | 函数名称 | 实现方式 | 计算结果 |
    | --- | --- | --- |
    | 加 | 2+3 | 5 |
    | 减 | 2-3 | -1 |
    | 乘 | 2*3 | 6 |
    | 除 | 2/3 | 0.6666666666666666 |
    | 取整除 | 2//3 | 0 |
    | 取余 | 2%3 | 2 |
    | 幂 | 2**3 | 8 |
    | 四舍五入 | round(pi) | 3 |
    | 向上取整 | math.ceil(pi) | 4 |
    | 向下取整 | math.floor(pi) | 3 |
    | 绝对值 | abs(-pi) | 3.14 |
    | 幂运算 | pow(pi, 2) | 9.8596 |
    | 开方 | math.sqrt(pi) | 1.772004514666935 |
    | 最大值 | max(x, y, z) | 3 |
    | 最小值 | min(x, y, z) | 1 |
    | 随机正整数 | random.randint(1, 6) | 2 |
    | 随机小数 | random.random() | 0.5334639240331638 |
    | 随机抽取 | random.choice(my_list) | paper |
    
    [Python编程基础：第六节 math包的基础使用Math Functions_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118682013)
    
    [Python编程基础：第二十八节 随机数Random Numbers_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118764359)
    
    - 强制类型转换
        
        [类型转换](https://www.notion.so/f06ef66f7a9647d6af40ee4ca54321a1)
        
        [Python编程基础：第四节 类型转换Type Cast_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118673173)
        
- format输出
    
    ```python
    animal = "cow"
    item = "moon"
    name = "Tom"
    number = 3.14159
    num = 1000
    ```
    
    | 输出格式 | 实现方式 | 输出结果 |
    | --- | --- | --- |
    | 占位符 | print("The {} jumped over the {}".format(animal, item)) | The cow jumped over the moon |
    | 指定顺序 | print("The {1} jumped over the {0}".format(animal, item)) | The moon jumped over the cow |
    | 指定变量名 | print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) | The cow jumped over the moon |
    | 指定变量打印位置宽度 | print("Hello, my name is {:10}. Nice to meet you".format(name)) | Hello, my name is Tom        . Nice to meet you |
    | 左对齐 | print("Hello, my name is {:<10}. Nice to meet you".format(name)) | Hello, my name is Tom        . Nice to meet you |
    | 右对齐 | print("Hello, my name is {:>10}. Nice to meet you".format(name)) | Hello, my name is          Tom. Nice to meet you  |
    | 居中对齐 | print("Hello, my name is {:^10}. Nice to meet you".format(name)) | Hello, my name is     Tom     . Nice to meet you |
    | 指定精度 | print("The number pi is {:.3f}".format(number)) | The number pi is 3.142 |
    | 三位一分割 | print("The number is {:,}".format(num)) | The number is 1,000 |
    | 二进制 | print("The number is {:b}".format(num)) | The number is 1111101000 |
    | 八进制 | print("The number is {:o}".format(num)) | The number is 1750 |
    | 十六进制 | print("The number is {:x}".format(num)) | The number is 3e8 |
    | 科学计数法 | print("The number is {:e}".format(num)) | The number is 1.000000e+03 |
    
    [Python编程基础：第二十七节 format输出Format_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118758259)
    
- f-string
    
    f-string的全称是插值格式字符串（interpolated format string），其语法是在格式字符串的前面加字母 `f` 作为前缀，我们可以直接在f-string的{ }里面引用当前Python范围内的所有名称以达到简化的目的，且{ }内冒号右侧所采用的规则与format输出保持一致，推荐使用这种方式作为字符串输出
    
    ```python
    key = 'number'
    value = 3.145
    places = 1
    ```
    
    | 输出格式 | 实现方式 | 输出结果 |
    | --- | --- | --- |
    | 字符串左对齐 | f'key = {key:<10}' | 'key = number     ' |
    | 数值保留小数点后两位 | f'value = {value:.2f}' | 'value = 3.15' |
    | 同时调用函数进行计算 | f'{key.title()}={round(value)}' | 'Number=3' |
    | 灵活的输出格式设定 | f'{value:.{places}f}' | '3.1' |
    | 直接插入计算表达式 | f"{3+2}" | '5' |
    | 数值转换为供解释器读取的形式x!r代表repr(x) | f'{value!r}' | '3.145' |
    | 数值转换为字符串x!s代表str(x) | f'{value!s}' | '3.145' |
    | 数值转换为字符串x!a代表ascii(x) | f'{value!a}' | '3.145' |
- print函数
    
    ```python
    f = open(r'a.txt', 'a')
    print('a', 'b', 'c', sep='\t', end=' ', file=f, flush=True)
    >>> a       b       c 
    ```
    
    ```markdown
    print(*values, sep=' ', end='\n', file=sys.stdout, flush=False)
    参数: *values -> 表示要打印的值
    			sep -> 表示当输入多个打印的值时，各个值之间分割方式， 默认空格
    			end -> 控制print中传入值输出完后结束符号，默认换行
    			file -> 可以设置file= 文件储存对象，把内容存到该文件中
    			flush -> 当flush=True时它会立即把内容刷新存到file中
    ```
    

### 0.2 基本逻辑

---

- if语句
    
    ```markdown
    if 条件1:
    		代码段1
    elif 条件2:
    		代码段2
    ......
    else:
    		代码段n
    ```
    
    也即先判断条件1，若满足则执行代码段1并跳出整个判断语句，否则判断条件2，若满足则执行代码段2并跳出整个判断语句，否则判断条件3……，若都不满足则执行代码段n。也即代码段1至代码段n只有一个会被执行
    
    ```python
    age = int(input("How old are you?: "))
    if age == 100:
        print("You are a century old!")
    elif age >= 18:
        print("You are an adult!")
    elif age < 0:
        print("You haven't been born yet!")
    else:
        print("You are a child!")
    >>> How old are you?: 100
    >>> You are a century old!
    ```
    
    [Python编程基础：第八节 判断语句If Statements_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118691440)
    
- for循环
    
    ```markdown
    for 判断1:
    		代码段1
    ```
    
    在for循环中我们可以更方便地控制循环次数以及终止条件
    
    ```python
    import time
    
    for seconds in range(10, 0-1, -1):
        print(seconds)
        time.sleep(1)
    print("Happy New Year!")
    >>> 10
    >>> 9
    >>> 8
    >>> 7
    >>> 6
    >>> 5
    >>> 4
    >>> 3
    >>> 2
    >>> 1
    >>> 0
    >>> Happy New Year!
    ```
    
    [Python编程基础：第十一节 for循环For Loops_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118698505)
    
- 循环控制语句
    - break是终止本层循环，比如你很多个while循环，你在其中一个while循环里写了一个break，满足条件，只会终止这个while里面的循环，程序会跳到上一层while循环继续往下走
    - continue是循环到这个点的时候，执行continue这里的某些操作，执行完了之后，继续循环满足条件的这一层循环需要做的事情，不会终止这一层循环。break/continue在嵌套循环中，只对最近的一层循环起作用
    - pass只是一个占位符，什么事情也不做
    
    ```python
    for i in range(2):
        for j in range(3):
            if j==1:
                break
            print(i, j)
    >>> 0 0
    		1 0
    for i in range(2):
        for j in range(3):
            if j==1:
                continue
            print(i, j)
    >>> 0 0
    		0 2
    		1 0
    		1 2
    for i in range(2):
        for j in range(3):
            if j==1:
                pass
            print(i, j)
    >>> 0 0
    		0 1
    		0 2
    		1 0
    		1 1
    		1 2
    ```
    
    [Python编程基础：第十三节 循环控制语句Loop Control Statements_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118699613)
    

- while循环
    
    ```markdown
    while 判断1:
    		代码段1
    ```
    
    当判断1为True时，while循环就会反复执行代码段1，直到判断1为False为止
    
    ```python
    name = None
    while not name:
        name = input("Enter your name: ")
    print("Hello {}".format(name))
    >>> Enter your name: 
    >>> Enter your name: Jon
    >>> Hello Jon
    ```
    
    [Python编程基础：第十节 while循环While Loops_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118692172)
    
- 嵌套循环
    
    ```markdown
    for 判断1:
    	for 判断2:
    		代码段1
    ```
    
    嵌套循环通常包括内循环与外循环，外循环执行一次，内循环执行一轮
    
    ```python
    rows = int(input("How many rows?: "))
    columns = int(input("How many columns?: "))
    symbol = input("Enter a symbol to use: ")
    for i in range(rows):
        for j in range(columns):
            print(symbol, end="")
        print()
    >>> How many rows?: 5
    >>> How many columns?: 6
    >>> Enter a symbol to use: $
    $$$$$$
    $$$$$$
    $$$$$$
    $$$$$$
    $$$$$$
    ```
    
    [Python编程基础：第十二节 嵌套循环Nested Loops_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118699059)
    
- 异常
    
    ```markdown
    try:
    		要检测异常信息的代码段
    except 异常信息1 as e:
    		要打印的报错信息1供程序员分析
    ......
    except 异常信息n as e:
    		要打印的报错信息n供程序员分析
    else:
    		如果要检测的代码段没有发生异常，那就执行这部分代码
    finally:
    		无论程序是否有异常，这里的代码均可以执行
    ```
    
    | 名称 | 说明 |
    | --- | --- |
    | AttributeError | 当你访问一个对象的属性，但是这个属性并没有在这个对象定义的时候，就会引发 AttributeError |
    | ImportError | 在使用 import 导入模块时，如果要导入的模块找不到，或者从模块中导入模块中不存在的内容。这时就会触发 ImportError 类型的错误或者它的子类 ModuleNotFoundError |
    | IndexError | 当你尝试从序列（如列表或元组）中检索索引，但是序列中找不到该索引。此时就会引发 IndexError |
    | KeyError | 与 IndexError 类似，当你访问映射(通常是 dict )中不包含的键时，就会引发 KeyError |
    | NameError | 当你引用了变量、模块、类、函数或代码中没有定义的其他名称时，将引发 NameError |
    | SyntaxError | 当代码中有不正确的 Python 语法时，就会引发 SyntaxError |
    | TypeError | 当你的代码试图对一个无法执行此操作的对象执行某些操作时，例如将字符串添加到整数中，以及一开始的例子使用 append 方法给元组添加元素，这些都会引发 TypeError |
    | ValueError | 当对象的值不正确时就会引发 ValueError。这个和我们前面说的因为索引的值不在序列的范围内，而导致 IndexError 异常类似 |
    | FileNotFoundError | 指定路径下不存在要读取的文件 |
    
    [Python编程基础：第二十九节 异常Exception_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118767592)
    
    [一文教你读懂Python中的异常信息](https://zhuanlan.zhihu.com/p/78029618)
    
    [python 一篇搞定所有的异常处理](https://www.cnblogs.com/wj-1314/p/8707804.html)
    

### 0.3 基本数据结构

---

- 列表
    
    用列表可以存储各种类型的数据
    
    ```python
    import random
    food = ["pizza", "hamburger", "hotdog", "spaghetti"]
    ```
    
    | 方法名称 | 实现方式 | 计算结果 |
    | --- | --- | --- |
    | 重新赋值 | food[0] = "sushi" | ['sushi', 'hamburger', 'hotdog', 'spaghetti'] |
    | 添加元素 | food.append("ice cream") | ['sushi', 'hamburger', 'hotdog', 'spaghetti', 'ice cream'] |
    | 合并两个列表元素 | food.extend(['ice']) | ['pizza', 'hamburger', 'hotdog', 'spaghetti', 'ice'] |
    | 查找元素 | 'pizza' in food | True |
    | 元素个数统计 | food.count('pizza') | 1 |
    | 剔除指定元素 | food.remove("hotdog") | ['sushi', 'hamburger', 'spaghetti', 'ice cream'] |
    | 剔除末尾元素 | food.pop() | ['sushi', 'hamburger', 'spaghetti'] |
    | 指定位置插入元素 | food.insert(0, "cake") | ['cake', 'sushi', 'hamburger', 'spaghetti'] |
    | 元素排序 | food.sort() | ['cake', 'hamburger', 'spaghetti', 'sushi'] |
    | 清空列表 | food.clear() | [] |
    | 切片 | food[:2] | ["pizza", "hamburger"] |
    | 查看变量是否为指定类型 | isinstance(food, (list, tuple)) | True |
    | 随机打乱 | random.shuffle(food) | ["pizza", "hotdog", "hamburger", "spaghetti"] |
    | 组合为字符串 | ','.join(food) | 'pizza,hamburger,hotdog,spaghetti' |
    
    [Python编程基础：第十四节 列表Lists_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118709241)
    
    [Python编程基础：第十九节 索引Index Operator_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118731343)
    
- 元组
    
    元组定义好以后，其中的元素是不能改变的
    
    ```python
    student = ("Bro", 21, "male")
    ```
    
    | 方法名称 | 实现方式 | 计算结果 |
    | --- | --- | --- |
    | 元素出现次数统计 | student.count("Bro") | 1 |
    | 元素索引查询 | student.index("male") | 2 |
    | 元素存在性查询 | "Bro" in student | True |
    
    [Python编程基础：第十六节 元组Tuple_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118710007)
    
- 字典
    
    字典中的元素互不相同
    
    ```python
    capitals = {"USA": "Washington DC", 
                "India": "New Dehli", 
                "China": "Beijing", 
                "Russia": "Moscow"}
    # 常见的遍历方式
    for key, value in capitals.items():
    		print("key=%s,value=%s" % (key, value))
    ```
    
    | 方法名称 | 实现方式 | 计算结果 |
    | --- | --- | --- |
    | 获取指定键的值 | capitals["Russia"] | Moscow |
    | 获取指定键的值，若不存在就返回"None"（推荐） | capitals.get("Germany", "None") | None |
    | 获取所有的键 | capitals.keys() | dict_keys(['USA', 'India', 'China', 'Russia']) |
    | 获取所有的值 | capitals.values() | dict_values(['Washington DC', 'New Dehli', 'Beijing', 'Moscow']) |
    | 获取键值对 | capitals.items() | dict_items([('USA', 'Washington DC'), ('India', 'New Dehli'), ('China', 'Beijing'), ('Russia', 'Moscow')]) |
    | 添加新的键值对 | capitals.update({"Germany": "Berlin"}) |  |
    | 添加新元素 | 变量名['键'] = 数据 | 这里的键是字典中不存在的 |
    | 修改元素 | 变量名['键'] = 数据 | 这里的键是字典中存在的 |
    | 剔除指定键值对 | capitals.pop("USA") |  |
    | 清空字典 | capitals.clear() | dict() |
    | 统计键值对个数 | len(capitals) | 4 |
    | 合并两个字典 | dictMerged2 = dict(dict1, **dict2) | dict2的key值为字符串时可用 |
    
    [Python编程基础：第十八节 字典Dictionaries_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118728783)
    
- 字典生成式
    
    字典生成式可以使用非常简洁的代码创建一个新的字典，在某些场合下可以替代for循环
    
    ```python
    # dictionary = {key: expression for (key, value) in iterable} (不包含条件判断)
    cities_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
    cities_C = {key: round((value-32)*(5/9)) for (key, value) in cities_F.items()}
    >>> {'New York': 0, 'Boston': 24, 'Los Angeles': 38, 'Chicago': 10}
    # dictionary = {key: expression for (key, value) in iterable if conditional} (包含if条件判断)
    cities_50 = {key: value for (key, value) in cities_F.items() if value>=50}
    >>> {'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
    # dictionary = {key: (if/else) for (key, value) in iterable if conditional} (包含if/else条件判断)
    cities_50 = {key: 'hot' if value>=50 else 'cold' for (key, value) in cities_F.items()}
    >>> {'New York': 'cold', 'Boston': 'hot', 'Los Angeles': 'hot', 'Chicago': 'hot'}
    # dictionary = {key: function(value) for (key, value) in iterable}
    def check_temp(value):
        if value>=70:
            return "hot"
        elif 40<=value<70:
            return "warm"
        else:
            return "cold"
    {key: check_temp(value) for (key, value) in cities_F.items()}
    >>> {'New York': 'cold', 'Boston': 'hot', 'Los Angeles': 'hot', 'Chicago': 'warm'}
    ```
    

- 二维列表
    
    ```python
    data = [[1, 2, 3], 
            [4, 5, 6]]
    data[0][:2]
    >>> [1, 2]
    ```
    
    ```python
    **# 超级实用的列表解套代码**
    from collections import Iterable
    # 递归调用
    flat = lambda t: [x for sub in t for x in flat(sub)] if isinstance(t, Iterable) and not isinstance(t, str) else [t]
    flat([[[1, 2], [3], [3, 4]], [1, 2]])
    >>> [1, 2, 3, 3, 4, 1, 2]
    ```
    
    [Python编程基础：第十五节 二维列表2D Lists_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118709679)
    
- 集合
    
    集合中的数据没有索引，没有顺序，互不相同
    
    ```python
    utensils = {"fork", "spoon", "knife", "knife"}
    dishes = {"bowl", "plate", "cup", "knife"}
    ```
    
    | 方法名称 | 实现方式 | 计算结果 |
    | --- | --- | --- |
    | 添加元素 | utensils.add("napkin") | {'napkin', 'spoon', 'knife', 'fork'} |
    | 剔除元素 | utensils.remove("fork") | {'napkin', 'spoon', 'knife'} |
    | 将一个集合合并到另一个集合 | utensils.update(dishes) | {'spoon', 'bowl', 'plate', 'napkin', 'knife', 'cup'} |
    | 并 | dinner_table = utensils.union(dishes) | {'cup', 'plate', 'bowl', 'spoon', 'knife', 'fork'} |
    | 差集 | diff = utensils.difference(dishes) | {'spoon', 'fork'} |
    | 交 | inter = utensils.intersection(dishes) | {'knife'} |
    | 清空元素 | utensils.clear() | set() |
    
    [Python编程基础：第十七节 集合Set_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118727536)
    
- 列表生成式
    
    列表生成式可以使用非常简洁的代码创建一个新的列表，在某些场合下可以替代for循环
    
    ```python
    # list = [expression for item in iterable] (不包含条件判断)
    squares = [i**2 for i in range(1, 11)]
    >>> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    # 可以模仿某些lambda函数
    students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    passed_students = list(filter(lambda x: x>=60, students))
    >>> [100, 90, 80, 70, 60]
    # list = [expression for item in iterable if conditional] (包含if条件判断)
    passed_students = [i for i in students if i>=60]
    >>> [100, 90, 80, 70, 60]
    # list = [expression for item in iterable if conditional] (包含if/else条件判断)
    students = [i if i>=60 else 'FAILED'  for i in students]
    >>> [100, 90, 80, 70, 60, 'FAILED', 'FAILED', 'FAILED', 'FAILED', 'FAILED']
    # 双重嵌套for循环
    [(i, j) for i in range(3) for j in range(3)]
    >>> [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    ```
    
- zip函数
    
    zip(*iterables)用于将可迭代的对象(list, tuples, sets, etc)作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的zip对象。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表
    
    ```python
    user = ['Alice', 'Bob', 'Tom']
    age = [12, 14, 15, 19]
    weight = [80.9, 76.4, 59,0]
    zip(user, age)
    >>> <zip object at 0x000001E14C0F9148>
    # 将zip对象转为列表
    list(zip(user, age))
    >>> [('Alice', 12), ('Bob', 14), ('Tom', 15)]
    # 将zip对象转为字典
    dict(zip(user, age))
    >>> {'Alice': 12, 'Bob': 14, 'Tom': 15}
    # 聚合3个可迭代对象
    list(zip(user, age, weight))
    >>> [('Alice', 12, 80.9), ('Bob', 14, 76.4), ('Tom', 15, 59)]
    # *解压
    list(zip(*zip(user, age)))
    >>> [('Alice', 'Bob', 'Tom'), (12, 14, 15)]
    ```
    

### 0.4 函数式编程

---

- 函数定义
    
    ```markdown
    def 函数名称(参数1, 参数2, 参数n):
    	函数体
    	return 返回对象
    ```
    
    函数的出现是为了简化代码，将重复书写部分变为一个可以调用的函数实例
    
    ```python
    # 默认参数放到最后
    def multiply(number1, number2=1):
        result = number1 * number2
        return result
    x = multiply(6, 8)
    # 指定关键字参数的调用方式
    x = multiply(number1=6, number2=8)
    >>> 48
    # 嵌套调用(类似于复合函数)
    import math
    math.pow(multiply(6, 8), 2)
    >>> 2304.0
    ```
    
    [Python编程基础：第二十一节 函数返回Return_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118733125)
    
    [Python编程基础：第二十二节 关键字参数Keyword Argument_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118750757)
    
    [Python编程基础：第二十三节 嵌套函数调用Nested Functions Calls_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118751056)
    
- 参数打包为元组
    
    args参数可以将用户指定的任意多个参数打包为一个**元组**传到函数中进行进一步运算
    
    ```python
    def test(*args):
        for i in args:
            print(i, end=' ')
    test(1, 2, 3, 4)
    >>> 1 2 3 4
    ```
    
    [Python编程基础：第二十五节 args参数*args_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118752514)
    
- 函数重命名
    
    `新的函数名称=旧的函数名称`，重命名后的新函数与原来函数功能相同
    
    ```python
    def Print_My_Name():
        print("This is my name")
    name = Print_My_Name
    name()
    >>> This is my name
    ```
    
    [Python编程基础：第五十一节 将函数赋值给变量Assign Functions to Variables_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/119103696?spm=1001.2014.3001.5501)
    
- 匿名函数
    
    书写方式为函数名称=lambda `参数列表:函数实现`，其中多个参数之间用逗号隔开，函数实现只能写一个语句，返回值就是该表达式的结果
    
    ```python
    # 运算
    add_numbers = lambda x, y, z: x + y + z
    print(add_numbers(1, 2, 3))
    >>> 6
    # 判断
    check_age = lambda age: True if age >= 18 else False
    print(check_age(12))
    >>> False
    ```
    
    ```python
    # 我们也可以将匿名函数用于类
    class temp:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2
        
        def sum_all(self):                # 两数相加
            return self.num1+self.num2
            
        def min_all(self):                # 两数相减
            return self.num1-self.num2
    
    func_ = lambda: temp(1, 2)            # 通过匿名函数，可以创建函数func_代替类temp
    func_real = func_()                   # 使用函数重命名得到相同功能函数func_real
    func_real.num2 = 10                   # 在类变量外部修改属性值
    print('{}'.format(func_real.sum_all())) # 基于函数调用类方法
    print('{}'.format(func_real.min_all()))
    >>> 11
    >>> -9
    ```
    
    [Python编程基础：第五十三节 匿名函数Lambda Function_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/119111819)
    
- reduce函数
    
    从左到右对一个序列的项累计地应用有两个参数的函数，以此合并序列到一个单一值。例如，reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])  计算的就是((((1+2)+3)+4)+5)
    
    ```python
    from functools import reduce
    li = [1,2,3,4,5,6,7,8,9]
    print(reduce(lambda x,y:x*y, li))
    # 结果=1*2*3*4*5*6*7*8*9 = 362880
    ```
    
    [Python编程基础：第五十七节 reduce函数Reduce_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/119131691)
    
- sorted函数
    
    sorted() 函数对所有可迭代的对象进行排序操作
    
    ```python
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(L, key = lambda x : x[1], reverse=True))
    # 按成绩从高到低排列
    >>> [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]
    ```
    
    [Python函数学习--匿名函数](https://www.cnblogs.com/xiao-apple36/p/8577727.html)
    
    [Python编程基础：第五十四节 排序Sort_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/119113042)
    

- 变量的生命周期
    
    ```python
    name = "Jon"         # 全局访问
    name2 = 'Jack'
    def Display_Name():
    		global name2     # 指向全局参数
        name = "Tom"     # 函数内部访问
    		name2 = 'Alice'  # 修改全局参数
        print(name)
    Display_Name()       # 访问函数内部
    print(name)          # 访问全局
    print(name2)
    >>> Tom
    >>> Jon
    >>> Alice
    ```
    
    [Python编程基础：第二十四节 作用域Scope_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118751741)
    
- 参数打包为字典
    
    kwargs参数将用户传入的参数打包为**字典**传入函数中用于进一步的计算
    
    ```python
    def test(**kwargs):
        for name, value in kwargs.items():
            print('参数名称: {}, 参数取值: {}'.format(name, value))
    test(name='kali', pw='kali')
    >>> 参数名称: name, 参数取值: kali
    		参数名称: pw, 参数取值: kali
    ```
    
    [Python编程基础：第二十六节 kwargs参数**kwargs_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118753211)
    
- 高阶函数
    
    高阶函数的使用包含两种情况，一种是将另一个函数作为参数，另一种是返回一个函数
    
    ```python
    # 将另一个函数作为参数
    def Lower(text):
        return text.lower()
    def Hello(func, text):
        text = func(text)
        return text
    print(Hello(Lower, "Hello"))
    >>> hello
    # 返回一个函数
    def Calculate(number1):
        number1 += 5
        def Sum(number2):
            return number1 + number2
        return Sum
    print(Calculate(1)(2))
    >>> 8
    ```
    
    [Python编程基础：第五十二节 高阶函数High Order Functions_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/119109856)
    
- map函数
    
    map函数的作用是将指定函数作用于一个可迭代对象内部的每一个元素，其表达方式为`map(function, iterable)`，第一个位置指定作用函数，第二个函数指定被作用对象，相当于
    
    ```python
    for i in iterable:
    	function(i)
    ```
    
    ```python
    li = [1,2,3,4,5,6,7,8,9]
    print(list(map(lambda x:x*x, li)))
    >>> [1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```
    
    [Python编程基础：第五十五节 map函数Map_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/119130868)
    
- filter函数
    
    filter函数的作用是对可迭代对象内部的元素按照特定条件进行过滤，其书写方式为`filter(function, iterable)`，第一个参数指定过滤方式，第二个参数指定被作用对象，其作用方式相当于
    
    ```python
    for i in iterable:
    	if i match function:
    		print(i)
    ```
    
    ```python
    li = [1, 2, 4, 5, 6, 9, 10, 15]
    print(list(filter(lambda x:x % 2==1, li)))  # [1, 5, 9, 15]
    ```
    
    [Python编程基础：第五十六节 filter函数Filter_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/119131218)
    
- 递归函数
    
    递归就是函数自己调用自己，所有递归一定要有终止条件，这又被称作递归出口，递归出口通常可用if语句来设置，计算机使用递归求解5!
    
    ```python
    def recursive_fact(n):
        if n <= 1 :                     # 递归出口
            return n
        return n * recursive_fact(n-1)  # 递归调用
    print(recursive_fact(5))
    >>> 120
    ```
    
    ```markdown
    求解过程: 
    ===> recursive_fact (5)                       递（去的过程）
    ===> 5 * recursive_fact (4)
    ===> 5 * (4 * recursive_fact (3))
    ===> 5 * (4 * (3 * recursive_fact (2)))
    **===> 5 * (4 * (3 * (2 * recursive_fact (1))))** 本层空间终止
    ===> 5 * (4 * (3 * (2 * **1**)))                  归（回的过程）
    ===> 5 * (4 * (3 * **2**))
    ===> 5 * (4 * **6**)
    ===> 5 * **24**
    ===> **120**
    ```
    
    [Python中的递归](https://zhuanlan.zhihu.com/p/158300209)
    

### 0.5 txt文件操作

---

- 文件检测
    
    检测指定路径下是否存在该文件
    
    ```python
    import os
    path = r"C:\Users\shen_student\Desktop\lyric.txt"
    ```
    
    | 函数名称 | 作用 | 返回 |
    | --- | --- | --- |
    | os.path.exists(path) | 判断我们指定的path是否存在 | True/False |
    | os.path.isfile(path) | 判断该路径指定的是否是一个文件 | True/False |
    | os.path.isdir(path) | 判断该路径指定的是否是一个文件夹 | True/False |
    
    [Python编程基础：第三十节 文件检测File Detection_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118768418)
    
- 文件写入
    
    ```python
    text = "Yoooooooooooooo\nThis is some text\nhave a good one!\n"
    path = r"C:\Users\shen_student\Desktop\lyric.txt"
    # w表示覆盖、a表示追加
    with open(path, mode="w", encoding="utf-8") as file:
    	file.write(text)
    ```
    
    - 我们可以编写辅助函数来确保程序收到的字符序列确实是期望操作的类型（要知道自己想操作的到底是Unicode码点，还是原始的8位值。用UTF-8标准给字符串编码，得到的就是这样一系列8位值）
    - 从文件中读取二进制数据（或者把二进制数据写入文件）时，应该用'rb'（'wb'）这样的二进制模式打开文件
    - 如果要从文件中读取（或者要写入文件中）的是Unicode数据，那么必须注意系统默认的文本编码方案。若无法肯定，可通过encoding参数明确指定
    - 编写Python程序的时候，一定要把解码和编码操作放在界面最外层来做，让程序核心部分可以使用Unicode数据来运作，这种办法通常叫做Unicode三明治。程序核心部分，应该用str类型来表示Unicode数据，并且不要锁定到某种字符编码上面。**这样可以让程序接受多种文本编码（例如Latin-1等），并把它们都转化成Unicode，也能保证输出的文本信息都是用同一种标准（最好是UTF-8）编码的**
    
    [Python编程基础：第三十二节 文件写入Write a File_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118770238)
    
- 文件移动
    
    ```python
    import shutil
    # 从src_path移动到targ_path
    shutil.move(src_path, targ_path)
    ```
    
    [Python编程基础：第三十四节 文件移动Move a File_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118784110)
    

- 文件读取
    
    ```python
    path = r"C:\Users\shen_student\Desktop\lyric.txt"
    with open(path, encoding="utf-8") as file:
    	data = file.read()
    	file.close()
    ```
    
    ```python
    # 查看计算机的默认编码格式
    import locale
    
    print(locale.getpreferredencoding())
    >>> cp936
    ```
    
    [Python编程基础：第三十一节 文件读取Read a File_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118769859)
    
- 文件复制
    
    ```python
    import shutil
    # 从src_path复制到targ_path
    shutil.copyfile(src_path, targ_path)
    ```
    
    [Python编程基础：第三十三节 文件复制Copy a File_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118783915)
    
- 文件删除
    
    ```python
    import shutil
    # 删除path路径文件夹及其子文件
    shutil.rmtree(path)
    ```
    
    [Python编程基础：第三十五节 文件删除Delete a File_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118784591)
    

### 0.6 JSON数据

---

- JSON定义
    
    JSON: JavaScript Object Notation是一种轻量级的数据交换格式，其文件扩展名为 `.json`，通常用作APIs或软件配置文件，JSON格式的数据几乎可以用于所有的编程语言，其支持的数据格式如下表
    
    | 数据格式 | 英文名称 | 示例 |
    | --- | --- | --- |
    | 字符串 | Strings | "Hello World"、"Kyle"、"I" |
    | 数值 | Numbers | 10、1.5、-30、1.2e10 |
    | 布尔型 | Booleans | true、false |
    | 空 | null | null |
    | 数组 | Arrays | [1, 2, 3]、["Hello", "World"] |
    | 对象 | Objects | {"key": "value"}、{"age": 30}这里的value可以是任意其它数据格式 |
    
    数据示例，JSON数据需要遵守如下规则: 
         数组或对象最后一个成员的后面，不能加逗号
         对象的键名必须放在双引号里面
         字符串必须使用双引号表示，不能使用单引号
    
    ```json
    {
    	"name": "Kyle", 
    	"number": 3, 
    	"isProgrammer": true, 
    	"hobbies": ["Bowling", "reading"], 
    	"friends": [{
    		"name": "Tom", 
    		"number": 10, 
    		"isProgrammer": false, 
    		"friends": [...]
    	}]
    }
    ```
    
- JSON数据保存到文件
    
    ```python
    def write_file(data, path):       
        with open(path, 'w', encoding='utf-8') as file_obj:
            json.dump(data, file_obj, indent=2, ensure_ascii=False)
    ```
    

- 数据解析
    - JSON → Python
        
        ```python
        import json
        
        # 定义一个字符串，其内容格式与字典相似
        people_string = '''
        {
            "people": [
                {
                    "name": "John", 
                    "phone": "615-555-7164", 
                    "emails": ["John@163.com", "John@gmail.com"],
                    "has_license": false
                }, 
                {
                    "name": "Jane", 
                    "phone": "560-555-5153", 
                    "emails": null, 
                    "has_license": true
                }
            ]
        }
        '''
        
        # 使用json.loads函数将python字符串解析为JSON格式数据
        data = json.loads(people_string)
        >>>	{'people': [{'name': 'John',
        		   'phone': '615-555-7164',
        		   'emails': ['John@163.com', 'John@gmail.com'],
        		   'has_license': False},
        		  {'name': 'Jane',
        		   'phone': '560-555-5153',
        		   'emails': None,
        		   'has_license': True}]}
        # 查看数据格式，不难发现JSON的Objects格式数据会被解析为Python的dict，所以dict的所有操作方式此处都适用
        print(type(data))
        >>> <class 'dict'>
        ```
        
        | JSON | Python |
        | --- | --- |
        | object | dict |
        | array | list |
        | string | str |
        | number (int) | int |
        | number (real) | float |
        | true | True |
        | false | False |
        | null | None |
    - Python → JSON
        
        ```python
        # 仍然使用上例的data，先对其数值做一定的修改
        data['people'][0]['name'] = 'Tom'
        
        # 使用json.dumps函数将dict转为JSON格式数据，设定缩进为2字符增强可读性，按键增序排列
        new_string = json.dumps(data, indent=2, sort_keys=True)
        print(new_string)
        >>>	{
        		  "people": [
        		    {
        		      "emails": [
        		        "John@163.com",
        		        "John@gmail.com"
        		      ],
        		      "has_license": false,
        		      "name": "Tom",
        		      "phone": "615-555-7164"
        		    },
        		    {
        		      "emails": null,
        		      "has_license": true,
        		      "name": "Jane",
        		      "phone": "560-555-5153"
        		    }
        		  ]
        		}
        ```
        
        | Python | JSON |
        | --- | --- |
        | dict | object |
        | list, tuple | array |
        | str | string |
        | int, float, int- & float-derived Enums | number |
        | True | true |
        | False | false |
        | None | null |
- 从文件读取JSON数据
    
    ```python
    def load_file(path):              
        with open(path, 'r', encoding='utf8') as fp:
            data = json.load(fp, strict=False)
        return data
    ```
    

### 0.7 面向对象编程

---

- 类
    
    ```markdown
    class 对象():
    	公共属性定义区域
    	def __init__(self, 属性1, 属性2, ..., 属性n):
    		self.属性1 = 属性1
    		......
    		self.属性n = 属性n
    	
    	def 方法1名称(self, 变量):
    		方法1具体执行方法
    	......
    	def 方法n名称(self, 变量):
    		方法n具体执行方法
    ```
    
    首先定义类（class）来表示对象，然后定义函数`__init__`来定义所有的属性，这里有一个关键字`self`表示这里的属性以及方法仅适用于当前类。然后通过定义多个函数对当前类的方法加以表示
    
    ```python
    class Student():
    		eyes = 2       # 所有学生都有两只眼睛
        # 初始化函数，用来完成一些默认的设定
        def __init__(self, name, height, home, school):
            self.name = name
            self.height = height
            self.home = home
            self.school = school
            
        def go_school(self):
            print("{} want to go {}".format(self.name, self.school))
            
        def go_home(self):
            print("{} want to go {}".format(self.name, self.home))
    ```
    
    [Python编程基础：第三十九节 面向对象编程Object Oriented Programming_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118887941)
    
    [Python编程基础：第四十节 类变量Class Variables_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118894180)
    
- 多继承
    
    多继承是指一个子类可以拥有多个父类，其所有父类的属性和方法都能被其调用。其中多个父类之间用逗号隔开
    
    ```markdown
    # 父类1
    class 父类1名称:
    	公共属性
    	def 父类1方法1(self):
    		方法具体实现
    # 父类2
    class 父类2名称:
    	公共属性
    	def 父类2方法1(self):
    		方法具体实现
    # 子类
    class 子类名称(父类1名称, 父类2名称):
    	def __init__(self, 子类属性列表)：
    		self.子类属性 = 子类属性
    	def 子类方法1(self):
    		方法具体实现
    ```
    
    ```python
    # 父类1
    class Carnivore:
        def c_eat(self):
            print("Eat meat")
    # 父类2
    class Herbivorous:
        def h_eat(self):
            print("Eat vegetable")
    # 子类
    class People(Herbivorous, Carnivore):
        pass
    ```
    
    [Python编程基础：第四十三节 多继承Multiple Inheritance_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118912730)
    
- 方法链
    
    方法链是指一个对象一次调用其自身的多个方法，通常写作`对象.方法1.方法2`，我们需要给每个方法返回`self`
    
    ```markdown
    class 类名称():
    	def 方法1(self):
    		方法1的实现
    		return self
    
    	def 方法2(self):
    		方法2的实现
    		return self
    ```
    
    ```python
    class Animal():
        def eat(self):
            print("The animal is eating")
            return self
        def sleep(self):
            print("The animal is sleeping")
            return self
        def run(self):
            print("The animal is running")
            return self
    animal = Animal()
    animal.eat().sleep().run()
    ```
    
    [Python编程基础：第四十五节 方法链Method Chaining_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118925919?spm=1001.2014.3001.5501)
    
- 抽象类
    
    抽象类就是一个模板，里面声明了子类必须定义的函数，但是对于每个函数都没有给出具体实现。所有函数的实现都是在子类中定义
    
    ```markdown
    from abc import ABC, abstractmethod
    
    class 类名称(ABC):
        @abstractmethod
        def 方法名称(self):
            pass
    ```
    
    ```python
    # 抽象类
    from abc import ABC, abstractmethod
    
    class People(ABC):
        @abstractmethod
        def gender(self):
            pass
    # 具体实现
    class Man(People):
        def __init__(self, height):
            self.height = height
            
        def gender(self, country):    # 可传参
            print("This is a {} man".format(country))
        
        def description(self):
            print("This man is {}cm".format(self.height))
    ```
    
    [Python编程基础：第四十七节 抽象类Abstract Classes_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118936115?spm=1001.2014.3001.5501)
    

- 继承
    
    ```markdown
    # 父类
    class 父类名称:
    	公共属性
    	def 父类方法1(self):
    		方法具体实现
    # 子类
    class 子类名称(父类名称):
    	def __init__(self, 子类属性列表)：
    		self.子类属性 = 子类属性
    	def 子类方法1(self):
    		方法具体实现
    ```
    
    定义好的子类不仅可以访问子类属性以及子类方法，还可以访问父类属性以及父类方法。我们通过继承的方式增强代码可读性的同时也提高可维护性。若不采用继承，那么每个子类定义就需要写很多重复的代码，当要求改变共同函数名称时，也需要逐一修改，采用继承直接在父类中修改即可
    
    ```python
    # 父类
    class Animal:
        live = True
        
        def eat(self):
            print("This animal is eating")
            
        def sleep(self):
            print("This animal is sleeping")
    # 子类
    class Rabbit(Animal):
        def __init__(self, feet):
            self.feet = feet
        def run(self):
            print("This rabbit is running")
    ```
    
    [Python编程基础：第四十一节 继承Inheritance_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118894806)
    
    [Python编程基础：第四十二节 多重继承Multi Level Inheritance_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118912447)
    
- 方法重写
    
    那么如果我们想在继承的过程中重新书写父类的某些方法，此时就用到了方法重写
    
    ```markdown
    class 父类:
    	def 父类方法1(self):
    		方法1的具体执行方式
    
    class 子类(父类):
    	def 父类方法1(self):
    		重写父类方法1的执行方式
    ```
    
    ```python
    # 父类
    class Animal:
        def eat(self):
            print("This animal is eating")
    # 子类
    class Rabbit(Animal):
        def eat(self):
            print("This rabbit is eating carrot")
    ```
    
    [Python编程基础：第四十四节 方法重写Method Overriding_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118925872?spm=1001.2014.3001.5501)
    
- super函数
    
    通常情况下，我们在子类中定义了和父类同名的方法，那么子类的方法就会覆盖父类的方法。而super关键字实现了对父类方法的改写(增加了功能，增加的功能写在子类中，父类方法中原来的功能得以保留)。也可以说，super关键字帮助我们实现了在子类中调用父类的方法
    
    ```python
    # 祖父类
    class animal(object):                       # 新式类
        def __init__(self, name):
            self.name = name
        
        def eat(self):
            print('{} is eating'.format(self.name))
            return self
    # 父类
    class action(animal):
        def __init__(self, name, action_name):
            super().__init__(name)              # 调用animal的__init__
            self.action_name = action_name
        
        def do_action(self):
            print('{} is {}'.format(self.name, self.action_name))
            return self 
    # 子类
    class tiger(action):
        def __init__(self, name, action_):
            super().__init__(name, action_)     # 调用action的__init__
        
        def eat(self):
            # 调用action从animal继承的eat
            # 调用action的do_action
            super().eat().do_action()        
    
    tiger = tiger('tiger', 'running')
    tiger.eat()
    >>> tiger is eating
    		tiger is running
    ```
    
    [Python编程基础：第四十六节 super函数Super Function_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118933678?spm=1001.2014.3001.5501)
    
- 类作为函数参数
    
    ```python
    class Car:
        def __init__(self, color=None):
            self.color = color
        def view(self):
            print("The Car's color is {}".format(self.color))
        
    def Change_Color(car, color):
        car.color = color
    
    car_1 = Car()                # 实例化
    Change_Color(car_1, "red")   # 传参
    car_1.view()
    >>> The Car's color is red
    ```
    
    [Python编程基础：第四十六节 super函数Super Function_wzy628810的博客-CSDN博客](https://blog.csdn.net/wzy628810/article/details/118933678?spm=1001.2014.3001.5501)
    
    [Python编程基础：第四十九节 鸭子类型Duck Typing_wzy628810的博客-CSDN博客_走路像鸭子叫起来像鸭子和编程什么关系](https://blog.csdn.net/wzy628810/article/details/119101391?spm=1001.2014.3001.5501)
    

### 0.8 线程及模块化编程

---

- `__name__`
    1. `__name__`是python的一个内置类属性，它天生就存在于一个 python 程序中
    2. 直接运行python程序时，`__name__`的值为`"__main__"`
    3. 而在其它程序中导入.py文件运行时，`__name__`的值为文件名，即模块名
    4. 因此依据该特性，最直接的作用就是，区分py文件直接被运行，还是被引入其他程序中
    
    ```python
    # test_1.py
    print(__name__)                              # 1
    
    if __name__ == '__main__':
        print("直接运行test_1.py文件")
    else:
        print("test_1.py文件被其他脚本调用")       # 2
    ```
    
    ```python
    # test_2.py
    import test_1
    
    print(__name__)                              # 3
    
    if __name__ == '__main__':
        print("直接运行test_2.py文件")            # 4
    else:
        print("test_2.py文件被其他脚本调用")
    ```
    
    ```python
    # 运行test_2.py，运行步骤见上述代码的注释
    >>> test_1
    >>> test_1.py文件被其他脚本调用
    >>> __main__
    >>> 直接运行test_2.py文件
    ```
    
    [python中 "__name__"的实际应用_xiaox的专栏-CSDN博客](https://blog.csdn.net/wosind/article/details/90728198)
    
- 线程
    
    线程就是一个独立的代码执行流程，多线程是通过协调每个线程轮流运行以实现并发性，多线程的应用是面向I /O密集型的，也即程序/任务大部分时间都在等待外部事件（用户输入，网页抓取），此时使用多线程(multithreading)
    
    [https://ss.html.cn/article/55/bf/95/55bf95db4652a35e43140db47ca5ae95.jpg-600](https://ss.html.cn/article/55/bf/95/55bf95db4652a35e43140db47ca5ae95.jpg-600)
    
    ```python
    import threading
    
    number = list(range(4))
    result = {}                 # 使用全局变量捕获各个线程的返回结果
    
    def sum(num, add, name):
        result[name] = [i+add for i in num]
    
    x = threading.Thread(target=sum, args=(number[:len(number)//2], 1, 'thread_1'))
    x.start()
    y = threading.Thread(target=sum, args=(number[len(number)//2:], 2, 'thread_2'))
    y.start()
    x.join()
    y.join()
    print(result)
    >>> {'thread_1': [1, 2], 'thread_2': [4, 5]}
    ```
    
    [](https://blog.csdn.net/wzy628810/article/details/121369751)
    
- 多进程
    
    多进程能够在不同的CPU核心上并行运行任务，可以绕过用于线程的GIL。多进程更适合密集计算相关任务以提高cpu的使用率，实验证明当跑满所有的CPU核心时速度是最快的
    
    ![http://img1.cppcns.com/images/2021/202108/onpwjoalh3l.png](http://img1.cppcns.com/images/2021/202108/onpwjoalh3l.png)
    
    ![http://img1.cppcns.com/images/2021/202108/qmi54gyhx0e.png](http://img1.cppcns.com/images/2021/202108/qmi54gyhx0e.png)
    
    ```python
    from multiprocessing import Process, cpu_count
    import time
    result = {}
    def counter(num_1, num_2, name):
        count = 0
        for i in range(num_1, num_2):
            count += i
        result[name] = count
        print(result)
    
    def main():
        print(cpu_count())  # 计算本机的CPU核心数目
        a = Process(target=counter, args=(0, 25000000, '进程1'))
        a.start()
        b = Process(target=counter, args=(25000000, 50000000, '进程2'))
        b.start()
        c = Process(target=counter, args=(50000000, 75000000, '进程3'))
        c.start()
        d = Process(target=counter, args=(75000000, 100000000, '进程4'))
        d.start()
    
        a.join()
        b.join()
        c.join()
        d.join()
        print('运行耗时: {} 秒'.format(time.perf_counter()))
    
    if __name__ == '__main__':
        main()
    >>> 4
    >>> {'进程3': 1562499987500000}
    >>> {'进程1': 312499987500000}
    >>> {'进程2': 937499987500000}
    >>> {'进程4': 2187499987500000}
    >>> 运行耗时: 5.9548173 秒
    ```
    
    [](https://blog.csdn.net/wzy628810/article/details/121378154)
    

- time模块
    
    时间处理模块
    
    ```python
    import time
    ```
    
    | 函数作用 | 实现方式 | 输出结果 |
    | --- | --- | --- |
    | 结构化输出当前时间 | time.localtime()                                                  | time.struct_time(tm_year=2021, tm_mon=11, tm_mday=16, tm_hour=9, tm_min=10, tm_sec=19, tm_wday=1, tm_yday=320, tm_isdst=0) |
    | 结构化输出当前时间对应的UTC时间 | time.gmtime() | time.struct_time(tm_year=2021, tm_mon=11, tm_mday=16, tm_hour=1, tm_min=17, tm_sec=15, tm_wday=1, tm_yday=320, tm_isdst=0) |
    | 返回系统的基准时间 | time.ctime(0) | 'Thu Jan 1 08:00:00 1970' |
    | 根据时间跨度计算具体日期（以秒为单位） | time.ctime(1000000) | 'Mon Jan 12 21:46:40 1970' |
    | 计算当前时刻距离系统基准时间过去了多少秒 | time.time() | 1637025541.3220704 |
    | 将结构化时间转换为与基准时间之间的差值 | time.mktime(time.localtime()) | 1637025693.0 |
    | 线程推迟指定的时间运行，单位为秒 | time.sleep(1) | 过1s后运行下一行代码 |
    | 指定结构化时间的输出格式 | time.strftime("%B %d %Y %H:%M:%S", time.localtime())
    time.ctime(time.time()) | 'November 16 2021 13:32:40' |
    | 将时间字符串解析为结构化输出 | time.strptime("20 April, 2020", "%d %B, %Y") | time.struct_time(tm_year=2020, tm_mon=4, tm_mday=20, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=111, tm_isdst=-1) |
    | 根据元组创建时间，元素顺序与struct_time一致 | time.asctime((2020, 4, 20, 4, 20, 0, 0, 0, 0)) | 'Mon Apr 20 04:20:00 2020' |
    | 根据元组指定时间计算其与基准时间的间隔 | time.mktime((2020, 4, 20, 4, 20, 0, 0, 0, 0)) | 1587327600.0 |
    - [ ]  struct_time元组元素说明：
        
        tm_year（年）→ 比如2011
        tm_mon（月）→ 1 - 12
        tm_mday（日）→ 1 - 31
        tm_hour（时）→ 0 - 23
        tm_min（分）→ 0 - 59
        tm_sec（秒）→ 0 - 59
        tm_wday（星期）→ 0 - 6（0表示周日）
        tm_yday（一年中的第几天）→ 1 - 366
        tm_isdst（是否是夏令时）→ 默认为-1
        
    - [ ]  时间格式字符串说明：
        
        %a - 简写的星期几
        %A - 星期名称(全称)
        %b - 缩写月份名
        %B - 完整的月份名称
        %c - 首选日期和时间表示
        %C - 世纪值(年份除以100，范围从00到99)
        %d - 每月第几天(01至31)
        %D -和 %m/%d/%y 一样
        %e - 月的一天(1〜31)
        %g - 类似 %G, 但没有世纪
        %G - 4位数年份对应ISO星期数(参见%V)。
        %h - 类似于 %b
        %H - 小时，采用24小时制(00〜23)
        %I - 小时，采用12小时制(00〜12)
        %j - 一年中的哪一天(001至366)
        %m - 月份(01〜12)
        %M - 分钟
        %n - 换行符
        %p - 根据给定的时间值判定上午或下午
        %r - 上午和下午(a.m 和 p.m)时间
        %R - 24小时制时间
        %S - 秒
        %t - 制表符
        %T - 当前时间，等于 %H:%M:%S
        %u - 工作日为数字(1至7)，星期一= 1。注：在Sun Solaris上 Sunday=1
        %U - 本年的周数，先从第一个星期日作为第一周的第一天
        %V - 本年度ISO 8601的周数(01到53)，其中第1周是在本年度至少4天的第一周，星期一作为一周的第一天
        %W - 本年周数，先从第一个星期一作为第一周的第一天
        %w - 一个星期中第几天，这是一个十进制数 Sunday=0
        %x - 无时间的日期表示
        %X - 无日期的首选时间表示
        %y - 无世纪的年份表示(00到99)
        %Y - 年份表示(包括世纪)
        %Z 或 %z - 时区或名称或缩写
        %% - 一个文字%字符
        
- 守护线程
    
    当程序中主线程及所有非守护线程执行结束时，未执行完毕的守护线程也会随之消亡，程序将结束运行。守护线程常用于以下场景：后台任务，垃圾回收，等待输入，长期运行的代码段等等
    
    ```python
    # 线程相关代码最好在VS Code中运行
    import threading
    import time
    
    nick_name = ''
    
    def get_request(nick_name, thread_name):
        if nick_name in ['小度小度', '小爱同学']:
            print(f"{thread_name}: {'我在'}")
        else:
            print(f"{thread_name}: {'请输入正确的唤醒词'}")
        time.sleep(2)
        print("等待2秒")
    
    nick_name = input('请输入用户名: ')
    x = threading.Thread(target=get_request, args=(nick_name, '守护线程'), daemon=True)
    x.start()
    >>> 请输入用户名: 小度小度
    >>> 守护线程: 我在
    # 可见没有输出"等待2秒"，这是因为此时主线程已经结束，守护线程随之结束
    ```
    
    [](https://blog.csdn.net/wzy628810/article/details/121376762)
    

### 0.9 常用标准库

---

- datetime
    
    ```python
    import datetime
    ```
    
    | 功能 | 函数 | 运行结果 | 备注 |
    | --- | --- | --- | --- |
    | 根据年月日创建时间 | date = datetime.date(2021, 9, 10) | 2021-09-10 | 传参不可以写09 |
    | 根据时分秒创建时间 | datetime.time(9, 30, 23) | 09:30:23 |  |
    | 根据年月日时分秒创建时间 | datetime.datetime(2021, 11, 12, 8, 10, 9) | 2021-11-12 08:10:09 |  |
    | 获取日期 | datetime.datetime(2021, 11, 12, 8, 10, 9).date() | 2021-11-12 |  |
    | 获取时间 | datetime.datetime(2021, 11, 12, 8, 10, 9).time() | 08:10:09 |  |
    | 获取当前年月日 | date = datetime.date.today() | 2021-11-19 |  |
    | 获取当前年 | datetime.date.today().year | 2021 |  |
    | 获取当前日 | datetime.date.today().day | 22 |  |
    | 获取当前星期Mon=0 | datetime.date.today().weekday() | 0 |  |
    | 获取当前星期Mon=1 | datetime.date.today().isoweekday() | 1 |  |
    | 计算从今天往前数7天的日期 | today = datetime.date.today()
    delta = datetime.timedelta(days=7)
    print(today-delta) | 2021-11-15 |  |
    | 计算从今天往后数7天的日期 | today = datetime.date.today()
    delta = datetime.timedelta(days=7)
    print(today+delta) | 2021-11-29 |  |
    | 计算两日期之间的时间间隔 | today = datetime.date.today()
    date2 = datetime.date(2021, 12, 10)
    print(today-date2) | 18 days, 0:00:00 |  |
    | 计算两日期之间的天数 | today = datetime.date.today()
    date2 = datetime.date(2021, 12, 10)
    print((today-date2).days) | 18 |  |
    | 计算两日期之间的秒数 | today = datetime.date.today()
    date2 = datetime.date(2021, 12, 10)
    print((today-date2).total_seconds()) | 1555200.0 |  |
    | 获取当前时刻的时间戳 | datetime.datetime.now() | 2021-11-22 07:37:14.934360 | 同样可以计算时差 |
    | 获取当前时刻的UTC时间戳 | datetime.datetime.utcnow() | 2021-11-21 23:38:08.578712 |  |
    | 将datetime转为字符串 | datetime.datetime.today().strftime('%B %d, %Y') | November 22, 2021 | 这里的格式输出符号与time模块一致 |
    | 将字符串转为datetime | datetime.datetime.strptime('July 26, 2016', '%B %d, %Y') | 2016-07-26 00:00:00 | 这里的格式输出符号与time模块一致 |
- **os**
    
    

- logging
    - 初步使用
        
        日志级别：默认分为六种日志级别（括号为级别对应的数值），NOTSET（0）、DEBUG（10）、INFO（20）、WARNING（30）、ERROR（40）、CRITICAL（50）。我们自定义日志级别时注意不要和默认的日志级别数值相同，logging 执行时输出大于等于设置的日志级别的日志信息，如设置日志级别是 INFO，则 INFO、WARNING、ERROR、CRITICAL 级别的日志都会输出
        · DEBUG：程序调试bug时使用
        · INFO：程序正常运行时使用
        · WARNING：程序未按预期运行时使用，但并不是错误，如:用户登录密码错误
        · ERROR：程序出错误时使用，如: IO操作失败
        · CRITICAL：特别严重的问题，导致程序不能再继续运行时使用，如:磁盘空间为空，一般很少使用
        · 默认的是WARNING等级，当在WARNING或WARNING之上等级的才记录日志信息
        
        ```python
        import logging
        
        # 日志输出的配置
        logging.basicConfig(
            filename='test.log',                              # 存储文件路径
            level=logging.DEBUG,                              # 最低级别
            format='[%(asctime)s] %(levelname)s: %(message)s',# 输出格式
        		datefmt="%Y-%M-%d %H:%M:%S"                       # 时间格式
            )
        
        def add(num_1, num_2):
            return num_1+num_2
        # 直接替换print函数
        logging.debug('result: {}'.format(add(1, 2)))
        >>> 会生成一个test.log文件，文件内容为
            [2021-25-23 08:25:15] DEBUG: result: 3
        ```
        
        常用format格式如下表
        
        | 变量 | 格式 | 变量描述 |
        | --- | --- | --- |
        | asctime | %(asctime)s | 将日志的时间构造成可读的形式，默认情况下是精确到毫秒，如 2018-10-13 23:24:57,832，可以额外指定 datefmt 参数来指定该变量的格式 |
        | name | %(name) | 日志对象的名称 |
        | filename | %(filename)s | 不包含路径的文件名 |
        | pathname | %(pathname)s | 包含路径的文件名 |
        | funcName | %(funcName)s | 日志记录所在的函数名 |
        | levelname | %(levelname)s | 日志的级别名称 |
        | message | %(message)s | 具体的日志信息 |
        | lineno | %(lineno)d | 日志记录所在的行号 |
        | pathname | %(pathname)s | 完整路径 |
        | process | %(process)d | 当前进程ID |
        | processName | %(processName)s | 当前进程名称 |
        | thread | %(thread)d | 当前线程ID |
        | threadName | %threadName)s | 当前线程名称 |
    - 进阶使用
        
        为每一个代码模块创建不同的日志输出
        
        ```python
        # pkg.py文件夹下的代码
        import logging
        
        logger = logging.getLogger(__name__)
        # 配置日志级别
        logger.setLevel(logging.INFO)
        # 配置日志格式
        formatter = logging.Formatter("[%(asctime)s] %(name)s %(levelname)s: %(message)s")
        # 日志存储位置
        file_handler = logging.FileHandler('pkg.log', encoding="GBK")
        file_handler.setFormatter(formatter)
        # 日志输出到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        
        logger.info(f'result = {3+2}')
        ```
        
        ```python
        # run.py文件夹下的代码
        import logging
        import pkg
        
        logger = logging.getLogger(__name__)
        # 配置日志级别
        logger.setLevel(logging.DEBUG)
        # 配置日志格式
        formatter = logging.Formatter("[%(asctime)s] %(name)s %(levelname)s: %(message)s")
        # 日志存储位置
        file_handler = logging.FileHandler('run.log', encoding="GBK")
        file_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        
        def divide(x, y):
            try:
                return x/y
            except ZeroDivisionError:
                logger.error('除零错误')
                return None
                
        logger.debug(f'计算结果是: {divide(1, 0)}')
        ```
        
        我们运行run.py可以发现终端打印
        
        ```python
        [2021-11-24 14:30:05,473] pkg INFO: result = 5
        ```
        
        同时生成两个文件 `pkg.log` 和 `run.log`
        
        ```
        > pkg.log
        [2021-11-24 14:30:05,473] pkg INFO: result = 5
        ```
        
        ```
        > run.log
        [2021-11-24 14:30:05,480] __main__ ERROR: 除零错误
        [2021-11-24 14:30:05,480] __main__ DEBUG: 计算结果是: None
        ```
        
- **urllib**
