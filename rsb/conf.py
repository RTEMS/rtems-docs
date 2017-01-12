import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.99'
release = '4.11.99'

project = "RTEMS Source Builder"

latex_documents = [
	('index', 'rsb.tex', u'RTEMS Source Builder', u'RTEMS Documentation Project', 'manual'),
]
