# -*- coding: utf-8 -*-
'''
私有成员变量和
'''


class A(object):
    username = None
    '''
    私有属性
    '''
    __psw = None

    def __init__(self, username, psw):
        self.username = username
        self.__psw = psw

    def get_psw(self):
        return self.__psw

    def __say(self):
        '''
        私有方法
        '''
        print  'I say nice to ', self.username


if __name__ == '__main__':
    a = A('Jayin', 12345)
    '''
    无法通过a.__psw 访问.实际上，Python是把__psw重名了前缀加上_类名
    如：这里a._A__psw 就可以访问了
    '''
    # print a.__psw #错误的
    # print a._A__psw #可以正常访问

    # 通过暴露接口来访问
    print a.get_psw()
    print a._A__psw  # 可以正常访问

    '''
    同样地，无法访问私有方法__say(),原理同上
    '''
    a._A__say()  # 通常我们不会这么做，只为了演示



