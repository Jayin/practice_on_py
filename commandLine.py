#encoding:utf-8
import  sys
#python test.py


def pull(*args):
    print args


opt = []
data= []
v = raw_input("command : ")
while v != 'exit':
    source = v.split(' ');
    print source
    v = raw_input('command : ')

print 'exit successfully!'

