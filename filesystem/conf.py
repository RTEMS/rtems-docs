import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.99'
release = '4.11.99'

project = "RTEMS Filesystem Design Guide"

latex_documents = [
	('index', 'filesystem.tex', u'RTEMS Filesystem Design Guide', u'RTEMS Filesystem Design Guide', 'manual'),
]
