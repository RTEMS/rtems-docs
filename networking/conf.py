import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.0'
release = '4.11.0'

project = "RTEMS Networking User Manual"

latex_documents = [
	('index', 'networking.tex', u'RTEMS Networking User Documentation', u'RTEMS Documentation Project', 'manual'),
]
