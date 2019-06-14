from concurrent.futures import ProcessPoolExecutor
import time

def return_future_result(message):
    time.sleep(2)
    return message

pool = ProcessPoolExecutor(max_workers=2)

future1 = pool.submit(return_future_result, ("hello"))
future2 = pool.submit(return_future_result, ("world"))

print(future1.done())
time.sleep(3)
print(future2.done())

print(future1.result())
print(future2.result())


# from concurrent.futures import ProcessPoolExecutor
  
# URLS = ['http://www.baidu.com', 'http://qq.com', 'http://sina.com']
  
  
# def task(url, index,timeout=10):
#     return index,url
     
# #在此例子中if __name__ == "__main__":一定要加，因为没有if __name__会在创建子进程的时候又会运行，导致错误
# if __name__ == "__main__": 
#     p = ProcessPoolExecutor(max_workers=3)
#     results = p.map(task, URLS,range(3))
#     p.shutdown(wait=True)
#     for ret,url in results:
#         print(ret,url)
#         