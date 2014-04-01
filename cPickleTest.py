#encoding:utf-8
#数据序列化，cPickle 比pickle快1000倍
import cPickle as P
import tc

shoplistFile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

# with file(shoplistFile, 'w') as f:
#     print P.dump(shoplist, f)


@tc.Test
def write():
    f = file(shoplistFile, 'w')
    P.dump(shoplist, f)
    f.close()

shoplist = range(1,20*10000)
write()


# with file(shoplistFile, 'r') as f:
#     print P.load(f)
