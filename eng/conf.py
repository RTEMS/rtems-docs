import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

project = "RTEMS Software Engineering"

latex_documents = [
    ('index',
     'eng.tex',
     u'RTEMS Software Engineering',
     u'RTEMS Documentation Project',
     'manual'),
]
