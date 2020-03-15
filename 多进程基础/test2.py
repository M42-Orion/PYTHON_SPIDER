from multiprocessing import Process
import time


'''
继承Process类
'''
class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print('Pid:' + str(self.pid) + 'LoopCout' + str(count))

if __name__ == "__main__":
    for i in range(2,5):
        p = MyProcess(i)
        p.daemon = True#当父进程结束后，子进程会自动被终止
        p.start()
        p.join()#让所有子进程都执行完了然后再结束

    print('Main process Ended')



