# encoding:utf-8

# 是一个输入密码的小程序，我们自己设定一个密码，如果用户输入正确，则显示正确，否则显示错误

import tkinter as tk

window = tk.Tk()

def check_password():
    password = "123456"
    entered_password = passwordEntry.get()
    if entered_password == password:
        confirmLabel.config(text="正确")
    else:
        confirmLabel.config(text="错误")

passwordLabel = tk.Label(window, text="请输入一个6位数字的密码: ")
passwordEntry = tk.Entry(window, show="*")
button = tk.Button(window, text="确认", command=check_password)
confirmLabel = tk.Label(window)

passwordLabel.pack()
passwordEntry.pack()
button.pack()
confirmLabel.pack()

window.mainloop()