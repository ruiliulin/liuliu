# 打印26个大写英文字母(26个字母代码参考习题课10)并封装
class UpperAlpha():
    # 打印大写字母A
    def a():
        for i in range(0, 5):
            for k in range(0, 4 - i):
                print(" ", end="")
            for j in range(0, i + 1):
                if i == 0 or i == 2 or j == 0 or j == i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母B
    def b():
        for i in range(3):
            for j in range(3):
                if j == 0 or j == 1 and (i == 0 or i == 3) \
                or j == 2 and (i == 1 or i == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        for i in range(4):
            for j in range(3):
                if j == 0 or j == 1 and (i == 0 or i == 3) \
                or j == 2 and (i == 1 or i == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母C
    def c():
        for i in range(6):
            for j in range(4):
                if j == 0 and (i != 0 and i != 5) \
                or j == 1 and (i == 0 or i == 5) \
                or j == 2 and (i == 0 or i == 5) \
                or j == 3 and (i == 4 or i == 1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母D
    def d():
        for i in range(4):
            for j in range(3):
                if j == 0 or j == 1 and (i == 0 or i == 3) \
                or j == 2 and (i == 1 or i == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母E
    def e():
        for i in range(5):
            for j in range(3):
                if j == 0 or i == 0 or i == 2 or i == 4:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母F
    def f():
        for i in range(5):
            for j in range(4):
                if j == 0 or i == 0 or i == 2 and j != 3:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母G
    def g():
        for i in range(6):
            for j in range(4):
                if j == 0 and (i != 0 and i != 5) \
                or j == 1 and (i == 0 or i == 5) \
                or j == 2 and (i == 0 or i == 5 or i == 3) \
                or j == 3 and (i == 4 or i == 1 or i == 3):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母H
    def h():
        for i in range(5):
            for j in range(4):
                if j == 0 or j == 3 or i == 2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母I
    def i():
        for i in range(8):
            for j in range(5):
                if j == 2 or j == 1 and (i == 0 or i == 7) \
                or j == 3 and (i == 0 or i == 7):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母J
    def j():
        for i in range(6):
            for j in range(4):
                if j == 0 and i == 4 or j == 1 and i == 5 \
                or j == 2 and i == 5 or j == 3 and i != 5:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母K
    def k():
        for i in range(7):
            for j in range(4):
                if j == 0 or j == 1 and (i == 2 or i == 4) \
                or j == 2 and (i == 1 or i == 5) \
                or j == 3 and (i == 0 or i == 6):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母L
    def l():
        for i in range(7):
            for j in range(4):
                if j == 0 or i == 6:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母M
    def m():
        for i in range(7):
            for j in range(7):
                if j == 0 and (i != 1 and i != 3 and i != 5) \
                or j == 1 and i == 2 or j == 2 and i == 4 \
                or j == 3 and i == 6 or j == 4 and i == 4 \
                or j == 5 and i == 2 \
                or j == 6 and (i != 1 and i != 3 and i != 5):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母N
    def n():
        for i in range(4):
            for j in range(4):
                if j == 0 or j == 1 and i == 1 \
                or j == 2 and i == 2 or j == 3:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母O
    def o():
        for i in range(6):
            for j in range(4):
                if j == 0 and (i != 0 and i != 5) \
                or j == 1 and (i == 0 or i == 5) \
                or j == 2 and (i == 0 or i == 5) \
                or j == 3 and (i != 0 and i != 5):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母P
    def p():
        for i in range(7):
            for j in range(4):
                if j == 0 or j == 1 and (i == 0 or i == 3) \
                or j == 2 and (i == 1 or i == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母Q
    def q():
        for i in range(6):
            for j in range(5):
                if j == 0 and (i != 0 and i != 5) \
                or j == 1 and (i == 0 or i == 5) \
                or j == 2 and (i == 0 or i == 5 or i == 3) \
                or j == 3 and (i != 0 and i != 5) \
                or j == 4 and i == 5:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母R
    def r():
        for i in range(6):
            for j in range(4):
                if j == 0 or j == 1 and (i == 0 or i == 3) \
                or j == 2 and (i == 1 or i == 2 or i == 4) \
                or j == 3 and i == 5:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母S
    def s():
        for i in range(6):
            for j in range(5):
                if j == 0 and (i == 1 or i == 4) \
                or j == 1 and (i == 0 or i == 2 or i == 5) \
                or j == 2 and (i == 0 or i == 5 or i == 3) \
                or j == 3 and (i == 1 or i == 4):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母T
    def t():
        for i in range(6):
            for j in range(5):
                if j == 2 or i == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母U
    def u():
        for i in range(6):
            for j in range(5):
                if j == 0 and i != 5 or j == 1 and i == 5 \
                or j == 2 and i == 5 or j == 3 and i == 5 \
                or j == 4 and i != 5:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母V
    def v():
        for i in range(5):
            for j in range(5):
                if j == 0 and i == 0 or j == 1 and i == 2 \
                or j == 2 and i == 4 or j == 3 and i == 2 \
                or j == 4 and i == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母W
    def w():
        for i in range(5):
            for j in range(9):
                if j == 0 and i == 0 or j == 1 and i == 2 \
                or j == 2 and i == 4 or j == 3 and i == 2 \
                or j == 4 and i == 0 or j == 5 and i == 2\
                or j == 6 and i == 4 or j == 7 and i == 2 \
                or j == 8 and i == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母X
    def x():
        for i in range(7):
            for j in range(7):
                if j == 0 and (i == 0 or i == 6) \
                or j == 1 and (i == 1 or i == 5) \
                or j == 2 and (i == 2 or i == 4) \
                or j == 3 and i == 3 \
                or j == 4 and (i == 2 or i == 4) \
                or j == 5 and (i == 1 or i == 5) \
                or j == 6 and (i == 0 or i == 6):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母Y
    def y():
        for i in range(7):
            for j in range(7):
                if j == 0 and i == 0 or j == 1 and i == 1 \
                or j == 2 and i == 2 \
                or j == 3 and (i != 0 and i != 1 and i != 2) \
                or j == 4 and i == 2 or j == 5 and i == 1 \
                or j == 6 and i == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印大写字母Z
    def z():
        for i in range(7):
            for j in range(7):
                if i == 0 or i == 6 and (i == 0 or i == 6) \
                or j == 1 and i == 5 or j == 2 and i == 4 \
                or j == 3 and i == 3 or j == 4 and i == 2 \
                or j == 5 and i == 1 or j == 6 and (i == 0 or i == 6):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

a = UpperAlpha
a.z()
