# 加法运算
print("请分别输入两个数字用于加法计算")

f_num = input("第一个数为：")
s_num = input("第二个数为：")

try:
    f_num = int(f_num)
    s_num = int(s_num)
except ValueError:
    print("请输入数字！")
else:
    answer = f_num + s_num
    print(answer)