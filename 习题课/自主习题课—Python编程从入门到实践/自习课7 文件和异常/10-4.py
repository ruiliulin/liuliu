# 访客名单
filename = 'guest_book.txt'

while True:
    i = input("请输入名字(输入任意正整数退出)：")
    if i.isdigit():
        break
    else:
        print("欢迎{}".format(i))
        with open(filename, 'a') as file_object:
            file_object.write('访问者：{}\n'.format(i))