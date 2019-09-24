# encoding:utf-8

# 用Tkinter写一个小游戏随机生成我们需要的名字
import tkinter as tk
import random

window = tk.Tk()

def random1():
    s1 = ["cats", "hippos", "cakes"]
    s = random.choice(s1)
    return s

def random2():
    s2 = ["eats", "has", "likes", "hates"]
    s = random.choice(s2)
    return s

def button_click():
    name = nameEntry.get()
    verb = random2()
    noun = random1()
    sentence = name + " " + verb + " " + noun
    result.delete(0, tk.END)
    result.insert(0, sentence)

nameLabel = tk.Label(window, text="Name: ")
nameEntry = tk.Entry(window)
button = tk.Button(window, text="生成随机名称", command=button_click)
result = tk.Entry(window)

nameLabel.pack()
nameEntry.pack()
button.pack()
result.pack()

window.mainloop()
