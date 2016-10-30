import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.0'
release = '4.11.0'

project = "RTEMS Source Builder Manual"

latex_documents = [
	('index', 'c_user.tex', u'RTEMS C Source Builder', u'RTEMS Documentation Project', 'manual'),
]
