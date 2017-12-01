# coding:utf-8

import concurrent.futures
import math
import os
import time
import hashlib
import multiprocessing

#name = r'D:\VM\Centos7\Centos7-000004-s004.vmdk'
name = r'X:\005.操作系统ISO\CentOS-6.8-x86_64-bin-DVD1to2\CentOS-6.8-x86_64-bin-DVD2.iso'
block = 1024 * 1024 * 100


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


def worker(data, md5):
    md5.update(data)


def do_work(jobs):
    md5 = hashlib.md5()
    while True:
        try:
            data = jobs.get()
            # 处理数据
            worker(data, md5)
            if jobs.empty():
                print('digest:{}'.format(md5.hexdigest()))
            #print('Processing data:{},pid:{}'.format(data, os.getpid()))
        except Exception as e:
            print(e)
        finally:
            jobs.task_done()



def add_jobs(jobs):
    with open(name, 'br') as f:
        while True:
            c = f.read(block)
            if c == b'':
                break
            jobs.put(c)


if __name__ == '__main__':
    t1 = time.time()
    main(concurrency=1)
    t2 = time.time()
    print('spend time:{}'.format(t2 - t1))
