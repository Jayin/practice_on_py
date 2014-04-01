#coding:utf-8
__author__ = 'Jayin Ton'

import time


class TC(object):
    def __init__(self, verbose=True):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print 'Time-consuming: %f ms' % self.msecs

def Test(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        secs = time.time() - start
        print  'Time-consuming: %f ms' % (secs * 1000)
    return wrapper


