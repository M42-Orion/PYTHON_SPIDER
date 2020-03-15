from multiprocessing import Process,Lock
import time


'''
Lock,当两个进程同时暂用资源的时候，会出现互斥的现象，可以通过加锁的操作。
当一个进程正在进行的时候对这个资源进行加锁阻止而后的进程继续。
'''
class MyProcess(Process):
    def __init__(self, loop,lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            self.lock.acquire()#加锁防止进程冲突
            print('Pid:' + str(self.pid) + 'LoopCout' + str(count))
            self.lock.release()#加锁防止进程冲突

if __name__ == "__main__":
    lock = Lock()
    for i in range(10,15):
        p = MyProcess(i,lock)
        p.start()
