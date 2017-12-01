# coding:utf-8
"""
1.多进程处理框架
2.使用进程池来处理任务。
3.这个框架的代码比用队列简单，但性能比较差。
性能差的原因可能是：每次分发任务时都要去寻找空闲的进程，时间花在了等待、调度、传参上，
而不是花在真丄的处理上。
而使用任务队列方式，由进程去寻找任务，大部门时间花在处理上。
由于例子中的计算差不复杂，处理时间与调度时间差不多，或者更小。
将ProcessPoolExecutor改成ThreadPoolExecutor，即可变成多线程版本。在框架代码所示的情况下，
多线程版本比多进程版本效率更高。cpu占用率更低。但不意味着其它的情况下也是如此
4.由于任务是通过迭代器生成的，所以不会存在内存问题。

"""
import concurrent.futures
import math
import os
import time


def main():
    do_jobs()


def do_jobs():
    futures = set()
    #with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for data in get_jobs():
            future = executor.submit(worker, data)
            futures.add(future)
        wait_for(futures)


def get_jobs():
    for i in range(100000):
        yield i


def worker(data):
    print('Processing data:{},pid:{}'.format(data, os.getpid()))
    #for _ in range(1000): math.exp(math.sin(math.pow(math.log(data), math.log(data))))
    return math.exp(math.sin(math.pow(math.log(data), math.log(data))))


def wait_for(futures):
    try:
        for future in concurrent.futures.as_completed(futures):
            """
            err = future.exception()
            if err is None:
                result = future.result()
                print('worker return:{}'.format(result))
            else:
                print('worker error:{}'.format(err))
            """
            pass
    except KeyboardInterrupt:
        for future in futures:
            future.cancle()


if __name__ == '__main__':
    t1 = time.time()
    main()
    t2 = time.time()
    print('spend time:{}'.format(t2 - t1))