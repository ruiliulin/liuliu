import threading
import time

class Llrthread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):
            num += 1
            msg = self.name + " set num to " + str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()

num = 0
# RLock 可重铸锁
mutex = threading.RLock()

def text1():
    for i in range(5):
        t = Llrthread()
        t.start()


if __name__ == '__main__':
    text1()


