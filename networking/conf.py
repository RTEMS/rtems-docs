import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

project = "RTEMS Networking User Manual"

latex_documents = [
    ('index',
     'networking.tex',
     u'RTEMS Networking User Manual',
     u'RTEMS Documentation Project',
     'manual'),
]
