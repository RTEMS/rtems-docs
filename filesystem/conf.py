import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

project = "RTEMS Filesystem Design Guide"

latex_documents = [('index',
                    'filesystem.tex',
                    u'RTEMS Filesystem Design Guide',
                    u'RTEMS Filesystem Design Guide',
                    'manual')]
