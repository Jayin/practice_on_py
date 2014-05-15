#coding:utf-8

from cmd import Cmd


class Mycmd(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = '&>>'

    def default(self, line):
        print 'no found-->default', line

    def do_help(self, arg):
        print arg

    def do_test(self, arg):
        if not arg:
            self.help_test()
        print arg

    def help_test(self):
        print 'help-->'

    def do_quite(self,arg):
        print 'exit..'
        return True

    #more helpful
    do_q = do_quite


    def emptyline(self):
        print "emptyline!"

if __name__ == '__main__':
    mycmd = Mycmd()
    intro = "Welcom to my comman line tool"
    mycmd.cmdloop(intro=intro)

