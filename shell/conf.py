import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

project = "RTEMS Shell Guide"

latex_documents = [
    ('index',
     'shell.tex',
     u'RTEMS Shell Guide',
     u'RTEMS Documentation Project',
     'manual'),
]
