import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

latex_documents = [
    ('index',
     'porting.tex',
     u'RTEMS Porting Guide',
     u'RTEMS Documentation Project',
     'manual'),
]
