'''
import math
# print(math)
# ceil() 向上取整操作
print(math.ceil(5.2))
print(math.ceil(5.01))

# floor() 向下取整操作
print(math.floor(5.01))
print(math.floor(5.9))

# 查看系统保留关键字，不可以用来当做变量的命名
import keyword
print(keyword.kwlist)

# round() 四舍五入操作，不是数学模块的函数，是Python内置函数
print(round(5.4))
print(round(5.5))
print(round(5.9))

# sqrt() 开平方，返回浮点数
print(math.sqrt(4))
print(math.sqrt(0.5))

# pow() 与幂运算差不多，计算一个数的几次方，有两个参数，第一个是底数，第二个是指数，返回浮点数
print(math.pow(4,3))
print(4**3)

# fabs() 对一个数获取其绝对值，返回浮点数
print(math.fabs(-4.3))
print(math.fabs(0))

# abs() 也是取绝对值，但不是数学模块的，是Python内置函数，返回值由本身类型而定
print(abs(-6.5))
print(abs(2))
print(abs(0))

# fsum() 对整个序列求和，返回浮点数
print(math.fsum([1,2,3,4,5]))


# sum() Python内置函数，求和，返回值由本身类型而定
print(sum([1,2,3,4,5]))

# modf() 将一个浮点数拆分成小数部分和整数部分组成元组，小数在前，整数在后
print(math.modf(4.5))
print(math.modf(0))
print(math.modf(5))

# copysign() 将第二个数的符号（正负号）传给第一个数，返回第一个数值的浮点数
print(math.copysign(2,-3))
print(math.copysign(-4,5))

# 打印自然对数e和π的值
print(math.e)
print(math.pi)

'''

import random

#for i in range(10):
    # random() 获取0-1之间的随机小数，包含0不包含1
    #print(random.random())
    #print(random.randint(1,8)) # 随机获取指定开始和结束之间的值，返回整形 不可迭代

    # random.randomrange() 随机获取指定开始和结束之间的整数值，可以指定间隔值
    #print(random.randrange(1,9,3))

    # uniform() 随机获取在指定范围内的值（包含小数）
    #print(random.uniform(1,10))

# choice() 随机获取列表中的值
#print(random.choice([2,343,65,77,32,55]))

'''
# shuffle() 随机打乱序列，返回值是None
list1 = [1,2,4,6,7,8,10]
print(list1)
random.shuffle(list1)
print(list1)
'''

''' 
# ASCII码转数字---------------ord()
print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))
# 数字转ASCII码---------------chr()
print(chr(65))
print(chr(90))
print(chr(97))
print(chr(122))
'''



