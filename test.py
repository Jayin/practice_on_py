#encoding:utf-8

import os
# print os.path
# for x in sys.path:
#     print x

# sqlite3 =  importlib.import_module('sqlite3Demo')



#
# import mysql.connector
# cnx = mysql.connector.connect(user='root', database='test',port=3307)
# cor = cnx.cursor(buffered=True)
# sql = 'select * from user'
# cor.execute(sql)
# for row in cor:
#     print row
# cnx.close()

# import os
# print(os.path.join('/Users/pilgrim/diveintopython3/examples/', 'humansize.py'))
# print('/Users/pilgrim/diveintopython3/examples/'+'humansize.py')


import types

x = 1
# print type(x) !=types.IntType
# print __file__
# print 'globals-->',globals()
# print 'locals-->',locals()

#%[(key)][flags][width][.precision]typecode
# print "%(key)-10s=%(value)4d" % dict(key = "a", value = 10)
#
# print r'{0}--{1}--{go}'.format('key','value',go='lol')


# from string import letters,digits,Template
# print letters
# print digits
# print Template

def which_is_null():
    l = list()
    if l:
        print 'size=0'
    else:
        print 'not null'


def muti_map():
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 2, 3, 4, 5, 6]
    print map(x, y)
    for (xx) in (x, y):
        print xx


# def test(num):
#     return '0' * (4 - len(str(num))) + str(num)


# print test(1)
# print test(12)
# print test(123)
# print test(1234)

import json


def filelist():
    print os.path.join(os.getcwd(), 'io')
    print os.listdir(os.path.join(os.getcwd(), 'io'))
    dirs = os.listdir(os.path.join(os.getcwd(), 'io'))
    # print ','.join(dirs).split(',')
    res = []
    for fs in dirs:
        res.append(fs.decode("gbk"))
    js = json.dumps({
        'result': res
    })
    print js

# filelist()

# print 'abcdeftghtiasdfasdfasd'.ljust(10,'*')

