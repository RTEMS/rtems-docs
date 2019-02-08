import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

project = "RTEMS Eclipse Manual"

latex_documents = [
    ('index',
     'eclipse.tex',
     u'RTEMS Eclipse Manual',
     u'RTEMS Documentation Project',
     'manual'),
]
