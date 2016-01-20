import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '1.0'
release = '5.0'

latex_documents = [
	('index', 'filesystem.tex', u'RTEMS Filesystem', u'RTEMS Documentation Project', 'manual'),
]
