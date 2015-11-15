import os
import sys

ass=sys.argv

def args(ubyek):
    return ubyek

def exe():
    try:
        for i in range(1,len(args(ass))):
            os.system('rm %s' % (args(ass)[i]))
    except Exception:
        print 'tidak ada file yang pelungguh inginkan'

if __name__=='__main__':
    exe()
