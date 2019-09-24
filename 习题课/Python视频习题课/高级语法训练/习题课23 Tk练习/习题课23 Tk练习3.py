# encoding:utf-8

# 一个猜数字的小游戏
# 让计算机随机生成一个整数，用户输入去猜这个整数，如果正确，分数加1，并让计算机显示正确数字
# 如果用户输入错误，则分数不变，还是让计算机显示正确的数字

import tkinter as tk
import random

window = tk.Tk()

# 定义全局变量
maxNu = 10
score = 0
rounds = 0

def button_click():
    global score
    global rounds

    try:
        guess = int(guessBox.get())
        if 0 < guess <= 10:
            result = random.randint(1, maxNu)
            if guess == result:
                score += 1
            rounds += 1
        else:
            result = "输入不合法"
    except:
            result = "输入不合法"

    resultLabel.config(text=result)
    scoreLabel.config(text=str(score) + "/" + str(rounds))
    guessBox.delete(0, tk.END)


resultLabel = tk.Label(window)
scoreLabel = tk.Label(window)
guessBox = tk.Entry(window)
guessLabel = tk.Label(window, text="请输入一个1到10之间的整数：")
button = tk.Button(window, text="确认", command=button_click)

scoreLabel.pack()
guessLabel.pack()
guessBox.pack()
resultLabel.pack()
button.pack()

window.mainloop()