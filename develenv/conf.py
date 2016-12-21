import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.99'
release = '4.11.99'

latex_documents = [
	('index', 'develenv.tex', u'RTEMS Development Environment Documentation', u'RTEMS Documentation Project', 'manual'),
]
