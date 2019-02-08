import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

project = "RTEMS User Manual"

latex_documents = [
    ('index',
     'user.tex',
     u'RTEMS User Manual',
     u'RTEMS Documentation Project',
     'manual'),
]
