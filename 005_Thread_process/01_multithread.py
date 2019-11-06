#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time,random


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        time.sleep(random.randint(0,10));
        print("Exiting"+self.name)


# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# # 开启线程
# thread1.start()
# thread2.start()

for i in range(1,10):
	myThread(i, "Thread-"+str(i), i).start()

for i in range(10):
	print("=========")

