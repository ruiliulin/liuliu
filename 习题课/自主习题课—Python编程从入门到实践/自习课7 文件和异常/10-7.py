# 加法计算器

while True:
    print("请分别输入两个数字用于加法计算(输入-1退出)")
    f_num = input("第一个数为：")
    if f_num == str(-1):
        break
    s_num = input("第二个数为：")
    if s_num == str(-1):
        break
    try:
        f_num = int(f_num)
        s_num = int(s_num)
    except ValueError:
        print("请输入数字！")
    else:
        answer = f_num + s_num
        print(answer)