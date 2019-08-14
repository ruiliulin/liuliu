# 记住喜欢的数字
import json
def remember_num():
    '''如果存储了用户名，就向用户显示它，否则让用户输入用户名'''
    filename = 'f_n.json'
    try:
        with open(filename) as f_obj:
            f_n = json.load(f_obj)
    except FileNotFoundError:
        f_n = input("What's your favourite number?")
        with open(filename, 'w') as f_obj:
            json.dump(f_n, f_obj)
    else:
        print("Your favourite number is {}".format(f_n))

remember_num()