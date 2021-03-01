import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

project = "RTEMS Legacy Networking User Manual"

latex_documents = [
    ('index',
     'legacy-networking.tex',
     u'RTEMS Legacy Networking User Manual',
     u'RTEMS Documentation Project',
     'manual'),
]
