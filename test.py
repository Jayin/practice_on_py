#encoding:utf-8

import os
import sys
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
print "%(key)-10s=%(value)4d" % dict(key = "a", value = 10)

print r'{0}--{1}--{go}'.format('key','value',go='lol')


from string import letters,digits,Template
print letters
print digits
print Template























