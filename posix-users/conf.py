import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

project = "RTEMS POSIX User Manual"

latex_documents = [('index',
                    'posix-users.tex',
                    u'RTEMS POSIX API User\'s Guide',
                    u'RTEMS Documentation Project',
                    'manual')]
