# coding:utf-8

import hashlib
import time


#name = r'D:\VM\Centos7\Centos7-000004-s004.vmdk'
name = r'X:\005.操作系统ISO\CentOS-6.8-x86_64-bin-DVD1to2\CentOS-6.8-x86_64-bin-DVD2.iso'
block = 1024*1024*100
start = time.time()
with open(name, 'br') as f:
    count = 0
    md5 = hashlib.md5()
    while True:
        c = f.read(block)
        if c == b'':
            print('md5:{}'.format(md5.hexdigest()))
            end = time.time()
            print('time spend:{}'.format(end-start))
            break
        else:
            count += 1
            md5.update(c)
            print('read content:{}'.format(count))
