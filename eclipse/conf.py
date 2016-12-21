import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.99'
release = '4.11.99'

project = "RTEMS Eclipse Manual"

latex_documents = [
	('index', 'eclipse.tex', u'RTEMS Eclipse Manual', u'RTEMS Documentation Project', 'manual'),
]
