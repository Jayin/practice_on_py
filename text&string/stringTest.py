#coding:utf-8

#比较字符串
s1 = 'abcddFe'
s2 = 'dd'
print cmp(s1, s2)  ##-1 if s1 > s2


#查找字符串
s1.index(s2)

#将字符串中的大小写转换
print s1.lower()
print s1.upper()

#翻转字符串
print s1[::-1]

#只显示字母与数字
def only_char_num(s, oth=''):
    s = s.lower();
    words = 'abcdefghijklmnopqrstuvwxyz013456789'
    for c in s:
        if not c in words:
            s = s.replace(c, '')
    return s


print only_char_num("a000 aa-b")