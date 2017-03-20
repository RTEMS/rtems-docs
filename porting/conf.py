import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

latex_documents = [
    ('index',
     'porting.tex',
     u'RTEMS Porting Guide',
     u'RTEMS Documentation Project',
     'manual'),
]
