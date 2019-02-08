import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

project = "RTEMS CPU Architecture Supplement"

latex_documents = [
    ('index',
     'cpu-supplement.tex',
     u'RTEMS CPU Architecture Supplement',
     u'RTEMS Documentation Project',
     'manual'),
]
