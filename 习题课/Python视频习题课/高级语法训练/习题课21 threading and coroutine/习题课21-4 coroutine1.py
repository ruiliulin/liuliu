# 使用协程的概念，达到以下目的：输入a, b, c, d四个整数，打印出(a+b)*(c+d)的值。
# 假设 a+b 和 c+d 是一个耗时1S的IO操作

import asyncio
import threading


async def sum(a, b):
    print("现在开始准备计算, 现在运行的线程是: {}".format(threading.currentThread()))
    r = int(a) + int(b)
    await asyncio.sleep(3)
    print("现在计算完啦, 此时运行的线程是: {}".format(threading.currentThread()))
    return r

loop = asyncio.get_event_loop()
task = asyncio.gather(sum(1, 2, ), sum(3, 4, ))
loop.run_until_complete(task)
r1, r2 = task.result()
print(int(r1)*int(r2))
loop.close()
