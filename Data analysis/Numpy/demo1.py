#encoding:utf-8

import csv


def reader_csv_demo1():
    with open('stock.csv', 'r', encoding='utf-8') as fp:
        # reader是一个迭代器
        reader = csv.reader(fp)
        next(reader) # 不会从第0行开始
        for i in reader:
            #print(i)
            name = i[3]
            volumn = i[-1]
            print({'name':name, 'volumn':volumn})

def reader_csv_demo2():
    with open('stock.csv', 'r', encoding='utf-8') as fp:
        # 使用Dictreader创建的reader对象不会包含标题那行的数据
        # reader是一个迭代器，遍历这个迭代器，返回来的是一个字典dict
        reader = csv.DictReader(fp)
        for r in reader:
            print({'name':r['secShortName'], 'volumn':r['turnoverVol']})

if __name__ == '__main__':
    reader_csv_demo2()
