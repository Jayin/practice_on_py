import cPickle as pickle


d = dict(age=1, name='Jayin Ton')

with open("test.txt", mode='w') as f:
    pickle.dump(d, f)
    print 'dump ok!'

with open('test.txt',mode='r') as f:
    content = pickle.load(f)
    print "conent-->",content


"""
dumps()函数执行和dump() 函数相同的序列化，但是与dump不同的dumps并不将转换后的字符串写入文件，而是将所得到的转换后的数据以字符串的形式返回。

loads()函数执行和load()函数一样的反序列化。 loads接受一个字符串参数，将字符串解码成为python的数据类型，函数loads和dumps进行的是互逆的操作。

cPickle是pickle得一个更快得C语言编译版本。

pickle的dump和load相当于java的序列化和反序列化操作
"""