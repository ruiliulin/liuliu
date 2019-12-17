#encoding: utf-8

import csv

def write_csv_demo1():
    headers = ['username', 'age', 'height']
    values = [
        ('张三', 18, 180),
        ('李四', 25, 190),
        ('王五', 28, 185)
    ]

    with open('classroom.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)

def write_csv_demo2():
    headers = ['username', 'age', 'height']
    values = [
        {'username':'张三', 'age':18, 'height':180},
        {'username':'李四', 'age':25, 'height':190},
        {'username':'王五', 'age':28, 'height':185}
    ]
    with open('classroom1.csv', 'w', encoding='utf-8', newline='') as fp:
        # 注意写入表头数据的时候，需要调用writeheader()的方法
        writer = csv.DictWriter(fp, headers)
        writer.writeheader()
        # 直接传入字典类型
        writer.writerows(values)


if __name__ == '__main__':
    write_csv_demo2()