import threading

sum = 0
loopSum = 1000000

def llr_add():
    global sum, loopSum
    for i in range(1, loopSum):
        sum += 1

def llr_minu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1

if __name__ == '__main__':
    print("Starting ...{}".format(sum))

    # 开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target=llr_add, args=( ))
    t2 = threading.Thread(target=llr_minu, args=( ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    '''
    每次顺序执行的结果都一样
    llr_add()
    llr_minu()
    '''
    print("Done ...{}".format(sum))
