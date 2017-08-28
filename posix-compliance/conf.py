import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

project = "RTEMS POSIX 1003.1 Compliance Guide"

latex_documents = [
    ('index',
     'rtems-posix1003-compliance.tex',
     u'RTEMS POSIX 1003.1 Compliance Guide',
     u'RTEMS Documentation Project',
     'manual'),
]
