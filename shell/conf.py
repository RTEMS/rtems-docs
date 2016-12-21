import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.99'
release = '4.11.99'

project = "RTEMS Shell Manual"

latex_documents = [
	('index', 'shell.tex', u'RTEMS Shell Documentation', u'RTEMS Documentation Project', 'manual'),
]
