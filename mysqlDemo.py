#encoding:utf-8
import mysql.connector
from mysql.connector import errorcode


DB_Name = 'test'
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': DB_Name,
    'port': 3307,
    'raise_on_warnings': True,
    # 'charset':'utf-8'
}


def checkDB():
    try:
        cnx = mysql.connector.connect(**config)
        print('db is ready.')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('账号or密码错误')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('数据库不存在')
        else:
            print(err)
    finally:
        cnx.close()


def setup():
    """
      create a table
      delete it if it's already exiest.
    """
    try:
        cnx = mysql.connector.connect(**config)
        sql_dropTable = 'drop table user'
        sql_createTable = 'create table user ' \
                          '(id varchar(10) primary key,' \
                          'username varchar(16),' \
                          'nickname varchar(16),' \
                          'psw varchar(16))'
        cursor = cnx.cursor()
        cursor.execute(sql_dropTable)
        cursor.execute(sql_createTable)
        cnx.close()
        print('setup is ok')
    except mysql.connector.Error as err:
        print(err)
    finally:
        cnx.close()

def insert(id,username,nickname,psw):
    try:
        cnx = mysql.connector.connect(**config)
        sql_insert = 'insert into user(id,username,nickname,psw) values(%s, %s, %s, %s)'
                     # 'values (%s, %s, %s, %s)'
        data = (id,username,nickname,psw)
        print data
        print sql_insert
        cursor = cnx.cursor()
        cursor.execute(sql_insert,data)
        print('insert ok')
    except mysql.connector.Error as err:
        print(err)
    finally:
         cnx.close()

def selectAll():
    try:
        cnx = mysql.connector.connect(**config)
        sql_select ='select * from user'
        cursor = cnx.cursor()
        cursor.execute(sql_select)
        for res in cursor:
            print res
        print('select finish!')
    except mysql.connector.Error as err:
        print(err)
    finally:
        cnx.close()
# checkDB()
# setup()
insert('11','jayint','jayin','123456')
insert('2222','mas','jayin','111')
selectAll()



