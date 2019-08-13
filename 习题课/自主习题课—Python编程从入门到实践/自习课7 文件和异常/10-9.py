# 沉默的猫和狗
def r_file(filename):
    try:
        with open(filename) as f_obj:
            f = f_obj.read()
    except FileNotFoundError:
        pass
    else:
            print(f)

l = ['cats.txt', 'dogs.txt']
for i in l:
    r_file(i)