# coding:utf-8
"""
通过迭代器列举目录中的所有文件
"""

import os


def get_files(dirs):
    """list all files and sub-directories in dirs"""
    for i in os.listdir(dirs):
        name = os.path.join(dirs, i)
        if os.path.isdir(name):
            for inner in get_files(name):
                yield inner
        yield name


def get_files2(pathname):
    """list all files and sub-directories in dirs"""
    for path,dirs,files in os.walk(pathname):
        for d in dirs:
            yield os.path.join(path,d)
        for f in files:
            yield os.path.join(path,f)


if __name__ == '__main__':
    gen = get_files2('F:\\')
    n = 0
    for i in gen:
        n += 1
        print(i)
    print(n)

