import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

latex_documents = [
    ('index',
     'posix1003-1.tex',
     u'RTEMS POSIX 1003.1 Compliance Guide',
     u'RTEMS Documentation Project',
     'manual'),
]
