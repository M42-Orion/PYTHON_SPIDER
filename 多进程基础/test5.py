from multiprocessing import Lock,Pool
import time


'''
在利用Python进行系统管理的时候，特别是同时操作多个文件目录，或者远程控制多台主机，并行操作可以节约大量的时间。当被操作对象数目不大时，可以直接利用multiprocessing中的Process动态成生多个进程，十几个还好，但如果是上百个，上千个目标，手动的去限制进程数量却又太过繁琐，此时可以发挥‘进程池’的功效。
Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来它。
'''

def function(index):
    print('Start process:',index)
    time.sleep(3)
    print('End process',index)

# #非阻塞
# if __name__ == "__main__":
#     pool = Pool(processes=3)
#     for i in range(4):
#         pool.apply_async(function,(i,))
#     print("Started procesddes")
#     pool.close()
#     pool.join()#让所有子进程都执行完了然后再结束
#     print("Subprocess done")

#阻塞
if __name__ == "__main__":
    pool = Pool(processes=3)
    for i in range(4):
        pool.apply(function,(i,))
    print("Started procesddes")
    pool.close()
    pool.join()#让所有子进程都执行完了然后再结束
    print("Subprocess done")
