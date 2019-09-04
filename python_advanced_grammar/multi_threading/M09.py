import time
import threading

# 1. 类需要继承自threading.Thread
class Llrthread(threading.Thread):
    """关于多线程的类"""
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    # 2. 必须重写run函数，run函数代表的是真正执行的功能
    def run(self):
        time.sleep(2)
        print("The args for this class is {}".format(self.arg))

for i in range(5):
    t = Llrthread(i)
    t.start()
    t.join()

print("Main thread is done!!!!!!!!!")
