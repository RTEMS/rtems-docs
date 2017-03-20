import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

project = "RTEMS C User Manual"

latex_documents = [('index',
                    'c-user.tex',
                    u'RTEMS C User Documentation',
                    u'RTEMS Documentation Project',
                    'manual')]
