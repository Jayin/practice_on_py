#coding:utf-8


class Animal(object):
    def __init__(self):
        self._birth = None

    @property     #getter
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @birth.deleter
    def birth(self):
        print 'del birth!'
        del self._birth  #这样才是真正的删除

    @property
    def age(self):
        return 2014 - self._birth


def main():
    a = Animal()
    a.birth = 1993  #调用 @birth.setter
    print a.age   #调用    @property
    del a.birth  #调用 @birth.deleter
    #print a.birth #


if __name__ == '__main__':
    main()