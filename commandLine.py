#encoding:utf-8
import sys
import os
#python test.py
cur_path = os.path.dirname(os.path.abspath('__file__'))


def cd():
    pass


def ls():
    print os.listdir(cur_path)
    print
ls()
# opt = []
# data = []
# print __file__
# print
# print os.listdir(os.path.realpath(os.curdir))
# print os.path
# # print os.path.splitdrive(os.path.curdir)
# print os.path.pardir
# print os.path.realpath(os.curdir)
# os.path.lexists


def run():
    v = raw_input("command : ")
    while v != 'exit':
        source = v.split(' ')
        print source
        v = raw_input('command : ')


print 'exit successfully!'

