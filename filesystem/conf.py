import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

project = "RTEMS Filesystem Design Guide"

latex_documents = [
    ('index',
     'filesystem.tex',
     u'RTEMS Filesystem Design Guide',
     u'RTEMS Filesystem Design Guide',
     'manual'),
]
