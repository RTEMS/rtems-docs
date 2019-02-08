import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

project = "RTEMS POSIX 1003.1 Compliance Guide"

latex_documents = [
    ('index',
     'posix-compliance.tex',
     u'RTEMS POSIX 1003.1 Compliance Guide',
     u'RTEMS Documentation Project',
     'manual'),
]
