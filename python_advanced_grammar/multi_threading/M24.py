import multiprocessing
import time


# 设置哨兵问题
def consumer(input_q):
    print("Into consumer:", time.ctime())
    while True:
        # 处理项
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q") # 此处替换为有用的工作
    # 下面一行执行完成，再转入主进程
    print("Out of consumer:", time.ctime())

def producer(sequence, output_q):
    print("Into producer:", time.ctime())
    for i in sequence:
        output_q.put(i)
        print("put", i, "into q")
    print("Out of producer:", time.ctime())

# 建立进程
if __name__ == '__main__':
    q = multiprocessing.Queue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target=consumer, args=(q, ))
    cons_p.start()

    # 生产多个项，sequence代表要发送给消费者的项序列
    # 在实践中，这可能是生成器的输出或者通过一些其他方式生产出来
    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    q.put(None)
    cons_p.join()