'''
利用time函数，生成两个函数
利用多线程调用
计算总的运行时间
练习带参数的多线程启动方法
'''

import time
# 导入多线程并更名为thread
import threading

def loop1(in1):
    # ctime得到当前时间
    print("Start loop 1 at:", time.ctime())
    # 把参数打印出来
    print("我是参数", in1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print("End loop 1 at:", time.ctime())

def loop2(in1, in2):
    # ctime得到当前时间
    print("Start loop 2 at:", time.ctime())
    # 把参数in1和in2打印出来，代表使用
    print("我是参数", in1, "和参数", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print("End loop 2 at:", time.ctime())

def main():
    print("Starting at:", time.ctime())
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("刘大拿", ))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("刘大拿", "周老师"))
    t2.start()

    # join等待多线程执行完毕后才会往下执行
    t1.join()
    t2.join()

    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)