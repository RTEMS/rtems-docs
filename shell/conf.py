import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.99'
release = '4.11.99'

project = "RTEMS Shell Guide"

latex_documents = [
	('index', 'shell.tex', u'RTEMS Shell Guide', u'RTEMS Documentation Project', 'manual'),
]
