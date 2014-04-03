#encoding:utf-8

#用importlib来加载
import  importlib
                              #name  package
tc =  importlib.import_module('tc','time-consuming')
import tc

@tc.Test
def work():
    pass