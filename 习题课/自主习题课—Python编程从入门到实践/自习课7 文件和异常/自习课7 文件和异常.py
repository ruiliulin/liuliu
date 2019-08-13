"""
# -1 从文件中读取数据
# 从文件中读取数据
# 读取整个文件
# 以下代码打开并读取文件pi_digits.txt，在将其内容显示到屏幕上
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())


# 绝对文件路径(最好不要有中文路径，容易报错)
# 相对文件路径是指在同一个文件夹下的查找不同文件的路径(子文件夹里的也不会查找！！！)
file_path = '/home/tlxy/tulingxueyuan/习题课/自主习题课—Python编程\
从入门到实践/oop/car.py'
with open(file_path) as file_object:
    content = file_object.read()
    print(content)


# 逐行读取
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        l = line
        print(l.rstrip())


# 创建一个包含文件各行内容的列表
filename = 'pi_digits.txt'

with open(filename) as file_object:
    # readline()从文件中读取每一行，并将其存储在一个列表中
    # 这样是为了在with代码块以外的地方也可以读取使用
    lines = file_object.readlines()
print(lines)
for l in lines:
    print(l.rstrip())


# 使用文件内容
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


# 百万型文件(打印出小数点后的前100位数)
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:102] + "...")
print(len(pi_string))


# 圆周率中包含你的生日吗？
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("请输入你的生日(全数字)：")
if birthday in pi_string:
    print("找到啦")
else:
    print("没找着")
"""


"""
# -2 写入文件
filename = 'programming.txt'

# 调用open时添加实参‘w'，以写入模式打开
with open(filename, 'w') as file_object:
    # 注意如果要写入的文件已经存在，Python将在返回文件对象前清空该文件(覆盖原来的文本内容)！
    # \n 用来换行
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')

# 附加模式’a'，不会先清空文件，而是附加到文件内容的末尾
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps.\n")
"""


"""
# -3 异常
# 处理ZeroDivisionError异常
# 0除数错误
# 使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# 使用异常避免崩溃
# 制作一个只有除法的简单计算器
# 使用try-except-else代码块抵抗错误异常
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# 处理FlieNotFoundError异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        f = f_obj.read()
except FileNotFoundError:
    msg = "sorry, the file {} doesn't exist".format(filename)
    print(msg)
else:
    # 计算文件大致有多少个单词
    # split()用给定的分隔符(默认空格)将字符串拆成多个并存储到列表中
    words = f.split()
    print("The file {} has about {} words.".format(filename, len(words)))
    
    
# 使用多个文件(定义函数方法)
def count_words(filename):
    '''计算一个文件大概包含多少个单词'''
    try:
        with open(filename) as f_obj:
            f = f_obj.read()
    except FileNotFoundError:
        msg = "sorry, the file {} doesn't exist".format(filename)
        print(msg)
    else:
        # 计算文件大致有多少个单词
        # split()用给定的分隔符(默认空格)将字符串拆成多个并存储到列表中
        words = f.split()
        print("The file {} has about {} words.".format(filename, len(words)))

filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt']
for f in filenames:
    count_words(f)


# 失败时一声不吭，pass跳过！！！
def count_words(filename):
    '''计算一个文件大概包含多少个单词'''
    try:
        with open(filename) as f_obj:
            f = f_obj.read()
    except FileNotFoundError:
        # 这里直接用pass跳过了
        pass
    else:
        # 计算文件大致有多少个单词
        # split()用给定的分隔符(默认空格)将字符串拆成多个并存储到列表中
        words = f.split()
        print("The file {} has about {} words.".format(filename, len(words)))

filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt']
for f in filenames:
    count_words(f)
"""


"""
# -4 存储数据（先做简单的了解，以后还会细讲）
# 使用json.dump()和json.load()
# 需要导入模块json
import json
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
print(numbers)
"""

# 加载信息
import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)




