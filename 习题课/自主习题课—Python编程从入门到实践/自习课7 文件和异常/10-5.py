# 关于编程的调查
filename = 'like_programme.txt'

while True:
    i = input("请问你为何喜欢编程？(输入-1退出)")
    if i == str(-1):
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write("喜欢编程的缘由：{}\n".format(i))