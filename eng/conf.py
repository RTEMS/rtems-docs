import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

project = "RTEMS Software Engineering Handbook"

latex_documents = [
    ('index',
     'software-engineering-handbook.tex',
     u'RTEMS Software Engineering Handbook',
     u'RTEMS Documentation Project',
     'manual'),
]
