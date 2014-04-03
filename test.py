#encoding:utf-8

import os
import sys


# print os.path
# for x in sys.path:
#     print x

# sqlite3 =  importlib.import_module('sqlite3Demo')




import mysql.connector
cnx = mysql.connector.connect(user='root', database='test',port=3307)
cor = cnx.cursor(buffered=True)
sql = 'select * from user'
cor.execute(sql)
for row in cor:
    print row
cnx.close()