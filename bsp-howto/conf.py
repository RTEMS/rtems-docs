import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

project = "RTEMS BSP and Driver Guide"

latex_documents = [
    ('index',
     'bsp-howto.tex',
     u'RTEMS BSP and Driver Guide',
     u'RTEMS Documentation Project',
     'manual'),
]
