#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 19:47
# @Author  : Scheaven
# @File    :  mult_processing.py
# @description:

import os

#注意此代码只适用于like Linux环境下

# print('进程{}%开始了...'.format(os.getpid()))
# pid = os.fork()
# if pid == 0:
#     print("我是子进程：{}%，我的父进程是：{}%".format(os.getpid(), os.getppid()))
# else:
#     print("本进程：{}%,只创造了一个子进程：{}%".format(os.getpid(), pid))



# from multiprocessing import Process
# import os


'''
在创建子进程的时候，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

'''
# import time
# #子进程要执行的代码
# def run_proc(name):
#     while 1:
#         print(name)
#         time.sleep(10000)
#         print('run child process {},{}'.format(name, os.getpid()))
#
# if __name__ == '__main__':
#     print ('parent process {}'.format(os.getpid()))
#     p = Process(target=run_proc,args=('test',))
#     pp = Process(target=run_proc, args=('wer',))
#     print( 'child process will start')
#     p.start()
#     pp.start()
#     print ('child process end')
#     print("=====================")


# from multiprocessing import Pool
# import os,time,random
#
#
'''
Pool（进程池）
如果我们要启动大量的子进程，可以用进程池的方式批量创建子进程：

'''
#
# #子进程要执行的代码
# def proc_task(name):
#     print ('运行子进程 {}号,（{}）'.format(name,os.getpid()))
#     start_time = time.time()
#     time.sleep(random.random()*3)#随机延时一波
#     end_time = time.time()
#     print ('子进程 %s 号 运行了 %0.2f 秒.' % (name, (end_time - start_time)))#此处为百分号占位符，和format作用一样
#
# if __name__ == '__main__':
#     print ("父进程是{}".format(os.getpid()))
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(proc_task,args=(i,))
#     print ("等待所有子进程执行完毕...")
#     p.close()
#     p.join()
#     print ("所有子进程执行完成")


from multiprocessing import Process,Queue
import os,time,random

'''
进程间的通信
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。python的multiprocessing模块包装了底层的机制，提供了Queue,Pipe等多种方式来交换数据。

在这里我们以较为常用的Queue为例子，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读取数据

作者：山有木兮有木兮
链接：https://www.jianshu.com/p/b8153cc83b44
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

#写数据进程
def write_data(q):
    print ('我是写入进程：{}'.format(os.getpid()))
    for v in ['a','b','c']:
        print ('把{}写入队列...'.format(v))
        q.put(v)
        time.sleep(random.random())

#读数据进程
def read_data(q):
    print ('我是读取进程：{}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print ('从队列里读取到{}...'.format(value))

if __name__ == '__main__':
    #父进程创建queue,并传递给各个子进程：
    q = Queue()
    pw = Process(target=write_data,args=(q,))
    pr = Process(target=read_data, args=(q,))
    #启动子进程pw,写入数据
    pw.start()
    #启动子进程pr，读取数据
    pr.start()
    #等待pw结束
    pw.join()
    #pr,进程里是死循环，无法等待其自动结束，所以手动结束
    pr.terminate()