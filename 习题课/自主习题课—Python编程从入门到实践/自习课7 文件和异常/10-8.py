# 猫和狗
"""
filename1 = 'cats.txt'
filename2 = 'dogs.txt'

with open(filename1, 'a') as f_obj:
    f_obj.write("miaomiao \n")
    f_obj.write("huahua \n")
    f_obj.write("ermiao \n")

with open(filename2, 'a') as f_obj:
    f_obj.write("tiaotiao \n")
    f_obj.write("huhu \n")
    f_obj.write("maomao \n")
"""

def r_file(filename):
    try:
        with open(filename) as f_obj:
            f = f_obj.read()
    except FileNotFoundError:
        print("{}这个文件没找到".format(filename))
    else:
            print(f)

l = ['cats.txt', 'dogs.txt']
for i in l:
    r_file(i)