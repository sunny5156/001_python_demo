from concurrent.futures import ThreadPoolExecutor
import time,random

def return_future_result(message):
    time.sleep(random.randint(1,10))
    return message

pool = ThreadPoolExecutor(max_workers=5)  # 创建一个最大可容纳2个task的线程池

# future1 = pool.submit(return_future_result, ("hello"))  # 往线程池里面加入一个task
# future2 = pool.submit(return_future_result, ("world"))  # 往线程池里面加入一个task

# print(future1.done())  # 判断task1是否结束
# time.sleep(3)
# print(future2.done())  # 判断task2是否结束

# print(future1.result())  # 查看task1返回的结果
# print(future2.result())  # 查看task2返回的结果

for i in range(1,10):
	print(pool.submit(return_future_result, i).result())

for i in range(10):
	print("=========")