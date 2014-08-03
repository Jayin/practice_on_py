#!/usr/bin/env python
#coding=utf-8
__author__ = 'Jayin Ton'


class A(object):
    '''
    1.共享对象 A.user_id即可访问，跟Java的static 定义也类似
    2.若从新赋值,则屏蔽了类变量，即不再是是共享变量
    '''
    user_id = 123

    def __init__(self):
        self.name = 'Code Monkey'  #类成员属性 ，对象实例化后才能访问
        pass

    @staticmethod  #类的全局函数，跟java的是类似的
    def go():
        print('Go GO!')

    @classmethod  #class相关的方法,class对象（不是class的实例对象）隐式地当作第一个参数传入，可以访问共享对象
    def say(cls):
        print('user_id = ' + str(cls.user_id))

    def sleep(self):
        print("sleepint~~~")
        print 'before-->',A.user_id
        A.user_id += 10


A.go()  #不需要实例化
A.say()  #不需要实例化
A().sleep()  #实例化才可以

print A.user_id  #输出为不需要实例化
