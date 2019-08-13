# 常见单词
def count_words(filename):
    try:
        with open(filename) as f_obj:
            f = f_obj.read()
    except FileNotFoundError:
        print("没有{}文件".format(filename))
    else:
        t = f.lower().count("the")
        print(t)

for i in ['little_women.txt', 'moby_dick.txt']:
    count_words(i)

