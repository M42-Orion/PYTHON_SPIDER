import multiprocessing

'''
class multiprocessing.Process(group=None, 
                              target=None, 
                              name=None, 
                              args=(), 
                              kwargs={}, 
                              *, 
                              daemon=None)
进程对象表示在单独进程中运行的活动。 Process 类等价于 threading.Thread 。

应始终使用关键字参数调用构造函数。 group 应该始终是 None ；它仅用于兼容 threading.Thread 。 target 是由 run() 方法调用的可调用对象。它默认为 None ，意味着什么都没有被调用。 
name 是进程名称。 
args 是目标调用的参数元组。 
kwargs 是目标调用的关键字参数字典。如果提供，则键参数 daemon 将进程 daemon 标志设置为 True 或 False 。如果是 None （默认值），则该标志将从创建的进程继承。
'''
def process(num):
    print('process',num)

if __name__ == "__main__":
    for i in range(5):
        p = multiprocessing.Process(target=process,args=(i,))
        p.start()

# import multiprocessing
# import time

# '''
# 可以通过 cpu_count() 方法还有 active_children() 方法获取当前机器的 CPU 核心数量以及得到目前所有的运行的进程。
# '''
# def process(num):
#     time.sleep(num)
#     print('Process:', num)

# if __name__ == "__main__":
#     for i in range(5):
#         p = multiprocessing.Process(target=process, args=(i, ))
#         p.start()
#     print('CPU number:'+ str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print('Child process name:'+ p.name+ 'id:'+ str(p.pid))
#     print('Process Ended')
