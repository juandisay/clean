import os
from glob import glob
import sys

ass=sys.argv[1]
subyek=glob('%s' %(ass))

try:
    for i in range(len(subyek)):
        os.system('rm %s'%(subyek[i]))
except:
    print 'file tidak tersedia'
