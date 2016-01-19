import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '1.0'
release = '5.0'

latex_documents = [
	('index', 'posix1003_1.tex', u'RTEMS POSIX 1003_1 Documentation', u'RTEMS Documentation Project', 'manual'),
]

