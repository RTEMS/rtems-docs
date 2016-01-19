import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '1.0'
release = '5.0'

latex_documents = [
	('index', 'shell.tex', u'RTEMS Shell Documentation', u'RTEMS Documentation Project', 'manual'),
]

