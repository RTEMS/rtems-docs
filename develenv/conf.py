import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

latex_documents = [
    ('index',
     'develenv.tex',
     u'RTEMS Development Environment Guide',
     u'RTEMS Documentation Project',
     'manual'),
]
