'''
# 练习
# 输入一个三位数与系统随机产生的三位数比较大小
# 1. 如果输入的三位数大于系统随机的三位数，则分别打印系统三位数的百位/十位/个位
# 2. 如果输入的三位数等于系统的三位数，则打印‘中大奖了’，并记录100分
# 3. 如果小于系统随机三位数；则将120个字符输入文本文件'随机三位数练习.txt'中
#（第3条的输入规则是每一条字符串的长度为12，单独占一行，并且前4个是字母，后8个是数字）
import random
def num_alpha():
    a_n = ""
    for i in range(4):
        i = random.randint(97,122)
        a_n = chr(i) + a_n
    fn = a_n
    for i in range(8):
        i = random.randint(1,9)
        fn = fn + str(i)
    l = fn
    return l
i = random.randint(100, 999)
num = input("请输入一个三位数：")
score = 0
if num.isdigit() and 100 <= int(num) <= 999:
    num = int(num)
    if num > i:
        print(i)
        print(i // 100)
        print(i % 100 // 10)
        print(i % 100 % 10 )# i % 10
    elif num == i:
           print("你中大奖啦")
           score += 100
           print(score)
    else:
        for i in range(10):
            a_num = num_alpha()
            # 执行文件存入操作
            with open('随机三位数练习.txt', 'a') as v:
                v.write(a_num + '\n')
else:
    print("请按要求输入一个三位数字")
'''

'''
# 循环小练习
import random

def num_game():
    score = 0
    times = 0
    while 1:
        num = random.randint(1, 3)
        i = input("请输入一个[1，2，3]区间内的整数(输入-1时退出)：")
        if int(i) == -1:
            break
        elif i.isdigit() and 1 <= int(i) <= 3:
            i = int(i)
            times += 1
            if i > num:
                print("你输入的数字大了！")
            elif i < num:
                print("你输入的数字小了！")
            else:
                print("恭喜你中奖啦！！！")
                score += 1
                print("你的中奖累计分数为：" + str(score*100))
                print("你的有效中奖率为："+ str(score/times))# 累计中奖次数/有效输入次数
        else:
            print("请按要求输入")
'''


'''
# 程序入口
if __name__ == '__main__':# 调试代码
    print(__name__)# 在本身模块中，__name__==__main__，第三方导入时__name__==文件名
    num_game()
'''

'''
import random
# 使用类封装
class NumGame():
    def num_game(self):
        score = 0
        times = 0
        while 1:
            num = random.randint(1, 3)
            i = input("请输入一个[1，2，3]区间内的整数(输入-1时退出)：")
            if int(i) == -1:
                break
            elif i.isdigit() and 1 <= int(i) <= 3:
                i = int(i)
                times += 1
                if i > num:
                    print("你输入的数字大了！")
                elif i < num:
                    print("你输入的数字小了！")
                else:
                    print("恭喜你中奖啦！！！")
                    score += 1
                    print("你的中奖累计分数为：" + str(score * 100))
                    print("你的有效中奖率为：" + str(score / times))
            else:
                print("请按要求输入")
'''

import random
class Numgame():

    def line(self):
        a_n = ""
        for i in range(4):
            i = random.randint(97, 122)
            a_n = chr(i) + a_n
        fn = a_n
        for i in range(8):
            i = random.randint(1, 9)
            fn = fn + str(i)
        l = fn
        return l

    def num_alpha(self):
        score = 0
        times = 0
        while True:
            i = random.randint(100, 999)
            num = input("请输入一个三位数(输入-1退出)：")
            if int(num) == -1:
                break
            elif num.isdigit() and 100 <= int(num) <= 999:
                num = int(num)
                times += 1
                if num > i:
                    print("输入的数字大啦!", i)
                    print(i // 100)
                    print(i % 100 // 10)
                    print(i % 10)
                elif num == i:
                    print("你中大奖啦!!!", i)
                    score += 1
                    print("你的中奖累计分数为：" + str(score*100))
                    print("你的有效中奖率为：" + str(score/times))
                else:
                    print("输入的数字小啦!", i)
                    for i in range(10):
                        a_num = Numgame.line(self)
                        # 执行文件存入操作
                        with open('随机三位数练习-14.txt', 'a') as v:
                            v.write(a_num + '\n')
            else:
                print("请按要求输入一个三位数字")



# 程序入口
if __name__ == '__main__':# 调试代码
    n = Numgame()
    n.num_alpha()