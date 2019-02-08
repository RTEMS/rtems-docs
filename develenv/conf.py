import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

project = "RTEMS Development Environment Guide"

latex_documents = [
    ('index',
     'develenv.tex',
     u'RTEMS Development Environment Guide',
     u'RTEMS Documentation Project',
     'manual'),
]
