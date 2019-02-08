import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

project = "RTEMS Classic API Guide"

latex_documents = [
    ('index',
     'c-user.tex',
     u'RTEMS Classic API Guide',
     u'RTEMS Documentation Project',
     'manual'),
]
