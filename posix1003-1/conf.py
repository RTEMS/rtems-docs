import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

latex_documents = [('index',
                    'posix1003-1.tex',
                    u'RTEMS POSIX 1003_1 Documentation',
                    u'RTEMS Documentation Project',
                    'manual')]
