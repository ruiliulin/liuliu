# 喜欢的数字
import json
filename = 'num.json'
num = input("输入你喜欢的数字：")
with open(filename, 'w') as f_obj:
    json.dump(num, f_obj)

with open(filename) as f_obj:
    num = json.load(f_obj)
    print("I know your favourite number! It's {}".format(num))