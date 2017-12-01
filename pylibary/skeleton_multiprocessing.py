# coding:utf-8
"""
1.多进程任务处理框架
2.将任务保存在jobs队列中，创建多个进程来处理jobs中的任务
最后使用join操作等待任务处理完成。
3.由于进程的daemon属性设置成True，当父进程退出时，各个子进程也会终止服务
4.这个模型适合处理计算密集型任务
5.在实际的使用过程中要注意，任务的添加速度与处理任务的速度之前的关系。若任务处理过慢，
有可能会占用大量的内存来保存未处理的任务，严重时会耗尽内存
"""
import multiprocessing
import os
import time
import random
import math
import time


def main(concurrency):
    jobs = multiprocessing.JoinableQueue()
    create_processes(concurrency, jobs)
    add_jobs(jobs)
    jobs.join()


def create_processes(concurrency, jobs):
    for _ in range(concurrency):
        process = multiprocessing.Process(target=do_work, args=(jobs,))
        # 当父进程退出时，终止子进程
        process.daemon = True
        process.start()
        print('create process,pid {}'.format(process.pid))


def worker(data):
    #for _ in range(1000): math.exp(math.sin(math.pow(math.log(data), math.log(data))))
    return math.exp(math.sin(math.pow(math.log(data), math.log(data))))


def do_work(jobs):
    while True:
        try:
            (data, ) = jobs.get()
            # 处理数据
            worker(data)
            print('Processing data:{},pid:{}'.format(data, os.getpid()))
        except Exception as e:
            print(e)
        finally:
            jobs.task_done()


def add_jobs(jobs):
    for i in range(100000):
        jobs.put((i,))


if __name__ == '__main__':
    t1 = time.time()
    main(concurrency=4)
    t2 = time.time()
    print('spend time:{}'.format(t2 - t1))
