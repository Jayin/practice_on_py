#coding:utf-8
#合并字符串
pieces = ['1', '2', '3', '4']
print ''.join(pieces)

pieces = [1, 2, 3, 4]
print ''.join(map(lambda x: str(x), pieces))

import operator

pieces = ['1', '2', '3', '4']
print reduce(operator.add, pieces, '')

pieces = ['1', '2', '3', '4']
print reduce(lambda x, y: x + y, pieces, '')

pieces = [1, 2, 3, 4]
print reduce(lambda x, y: x + str(y), pieces, '')

#字符串翻转
strs = '1234567'
print strs[::-1]

#为啥无效？
s = '1 2 3 4 5 6 7'
rewords = s.split()
print(rewords)
rewords.reverse()
print(rewords)
print '-'.join(rewords)

#检查字符串里是否出现某个子字符串
son = 'bbc'
dady = 'aaabbccdd'
print son in dady