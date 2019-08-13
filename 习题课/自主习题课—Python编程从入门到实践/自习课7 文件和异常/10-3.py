# 访客
filename = 'guest.txt'

i = input("请输入名字：")
with open(filename, 'a') as file_object:
    file_object.write('{} \n'.format(i))
