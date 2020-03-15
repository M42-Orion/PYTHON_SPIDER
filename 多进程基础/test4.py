from multiprocessing import Process,Semaphore,Lock,Queue
import time


'''
信号量，实在进程同步过程种，可以控制临界资源的熟练那个，保证进程之间互斥和同步
'''
buffer = Queue(10)
empty = Semaphore(2)
full = Semaphore(0)
lock = Lock()

class Consumer(Process):
    def run(self):
        global buffer,empty,full,lock
        while True:
            full.acquire()
            lock.acquire()
            buffer.get()
            print('Consumer pop an element')
            time.sleep(1)
            lock.release()
            empty.release()

class Producer(Process):
    def run(self):
        global buffer,empty,full,lock
        while True:
            empty.acquire()
            lock.acquire()
            buffer.put(1)
            print('Producer oppend an element')
            time.sleep(1)
            lock.release()
            full.release()

if __name__ == "__main__":
    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Ended')
