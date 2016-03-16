import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.0'
release = '4.11.0'

project = "RTEMS POSIX User Manual"

latex_documents = [
	('index', 'posix_users.tex', u'RTEMS POSIX API User\'s Guide', u'RTEMS Documentation Project', 'manual'),
]
