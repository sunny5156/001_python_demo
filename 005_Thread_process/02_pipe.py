# #!/usr/bin/env python
# # -*- encoding: utf-8 -*-
# '''
# @File	:   test_main.py
# @Time	:   2021/11/23 18:48:06
# @Author  :   Scheaven 
# @Version :   1.0
# @Contact :   snow_mail@foxmail.com
# @License :   (C)Copyright 2021-2022, Scheaven 360
# @Desc	:   注意要想接受端不卡顿，需要发送端close,并且需要他们在同一个进程之中（或者接收端需要感受到发送端已经关闭pipe,否则会一直卡主而不是报错）
# '''

# here put the import lib
import multiprocessing
import time
import random
from threading import Thread


def proc_send(pipe):
	 """
	 发送消息
	 :param pipe:管道一端
	 :return:
	 """
	 i=0
	 while i<999:
		 i+=1
		 pipe.send(i)
		 print("+++++++++size {} send:{}".format(1, str(i)))

	 pipe.close()

def proc_recv(pipe):
	 """
	 接收消息
	 :param pipe:管道一端
	 :return:
	 """
	 while True:
		 try:
			 print("---------size {}--- recv:{}".format(1, pipe.recv()))
			 time.sleep(random.random())
		 except EOFError as e:
			 print("end", e)
			 break



if __name__ == '__main__':

	 # 主进程创建pipe
	 pipe = multiprocessing.Pipe(False)
	#  p1 = multiprocessing.Process(target=proc_send,args=(pipe[0], ))
	 p1 = Thread(target=proc_send,args=(pipe[1], ))
	#  p2 = multiprocessing.Process(target=proc_recv,args=(pipe[1], ))
	 p2 = Thread(target=proc_recv,args=(pipe[0], ))
	 p1.start()
	 p2.start()

	 p1.join()
	#  pipe[0].close()
	 print("sdfsfd")
	 p2.join()

	 print("结束了")
